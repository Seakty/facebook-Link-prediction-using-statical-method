import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pickle  # <--- Don't forget to import this!

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Link Prediction Demo",
    page_icon="🔗",
    layout="wide"
)

# --- 1. LOAD DATA (From your .pkl file) ---
@st.cache_resource
def load_graph():
    filename = "graph_data.pkl"  # Your file name
    try:
        # We open the pickle file in 'read binary' (rb) mode
        with open(filename, 'rb') as f:
            G = pickle.load(f)
        dataset_name = "My Pre-trained Graph (PKL)"
        
        # quick check to ensure it loaded a Graph object
        if not isinstance(G, nx.Graph):
            st.error("The .pkl file does not contain a NetworkX Graph!")
            return nx.Graph(), "Error"
            
    except FileNotFoundError:
        st.error(f"Could not find {filename}. Please check the file path.")
        # Fallback just so the app doesn't crash
        G = nx.karate_club_graph()
        dataset_name = "Facebook Ego Networks"
        
    return G, dataset_name

G, dataset_name = load_graph()

# --- 2. SIDEBAR ---
st.sidebar.title("🔮 Prediction Settings")
st.sidebar.info(f"**Dataset:** {dataset_name}\n\n**Nodes:** {len(G.nodes())}\n**Edges:** {len(G.edges())}")

# User Input
all_users = sorted(list(G.nodes()))
selected_user = st.sidebar.selectbox("Select a User to Analyze", all_users)
top_k = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# --- 3. RECOMMENDATION ENGINE ---
def get_recommendations(user_id, graph, k=5):
    # Get current friends
    current_friends = set(graph.neighbors(user_id))
    
    # Get candidates (Anyone not me and not my friend)
    all_nodes = set(graph.nodes())
    candidates = list(all_nodes - current_friends - {user_id})
    
    # Calculate Adamic-Adar Scores
    # (We filter to only score candidates who actually share neighbors to speed it up)
    # A candidate needs at least 1 mutual friend to be worth scoring
    valid_candidates = []
    for cand in candidates:
        if len(list(nx.common_neighbors(graph, user_id, cand))) > 0:
            valid_candidates.append(cand)
            
    # Run AA Index
    preds = nx.adamic_adar_index(graph, [(user_id, cand) for cand in valid_candidates])
    
    # Sort
    sorted_preds = sorted(preds, key=lambda x: x[2], reverse=True)
    return sorted_preds[:k], current_friends

# --- 4. MAIN DASHBOARD ---
st.title("🔗 Social Link Predictor")
st.markdown("### Predicting *'People You May Know'* using Graph Topology")

# Run Logic
recommendations, current_friends = get_recommendations(selected_user, G, top_k)

# Display User Stats
col1, col2, col3 = st.columns(3)
col1.metric("Selected User ID", f"#{selected_user}")
col2.metric("Current Friends", len(current_friends))
col3.metric("Candidates Scored", len(G.nodes()) - len(current_friends) - 1)

st.divider()

# --- 5. RESULTS SECTION ---
row1, row2 = st.columns([1, 2])

with row1:
    st.subheader("🎯 Top Recommendations")
    
    if recommendations:
        # Create a nice DataFrame for display
        data = []
        for rank, (u, v, score) in enumerate(recommendations, 1):
            # Calculate mutual friends count just for display context
            mutual = len(list(nx.common_neighbors(G, u, v)))
            data.append({
                "Rank": rank,
                "User ID": v,
                "Score": round(score, 3),
                "Mutual Friends": mutual
            })
        
        df = pd.DataFrame(data)
        st.dataframe(
            df.set_index("Rank"), 
            use_container_width=True,
            column_config={
                "Score": st.column_config.ProgressColumn(
                    "Link Probability (Score)",
                    format="%.3f",
                    min_value=0,
                    max_value=max(d["Score"] for d in data) * 1.2
                )
            }
        )
    else:
        st.warning("No recommendations found (User might be isolated).")

with row2:
    st.subheader("🕸️ Network Visualization")
    
    if recommendations:
        # Visualize the #1 Recommendation
        top_rec = recommendations[0][1] # Get ID of #1 result
        
        # Create a subgraph: User + Top Rec + Mutual Friends
        mutual_friends = list(nx.common_neighbors(G, selected_user, top_rec))
        
        # Limit mutual friends to 15 to keep graph clean
        subset_nodes = [selected_user, top_rec] + mutual_friends[:15]
        subgraph = G.subgraph(subset_nodes)
        
        # Draw
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(subgraph, seed=42)
        
        # Draw Nodes
        # 1. The Main User (Blue)
        nx.draw_networkx_nodes(subgraph, pos, nodelist=[selected_user], node_color='#3498db', node_size=800, label="Me")
        # 2. The Recommended Friend (Green)
        nx.draw_networkx_nodes(subgraph, pos, nodelist=[top_rec], node_color='#2ecc71', node_size=800, label="Recommendation")
        # 3. The Mutual Friends (Grey)
        nx.draw_networkx_nodes(subgraph, pos, nodelist=mutual_friends[:15], node_color='#95a5a6', node_size=300, label="Mutual Friends")
        
        # Draw Edges
        nx.draw_networkx_edges(subgraph, pos, alpha=0.3)
        
        # Labels
        nx.draw_networkx_labels(subgraph, pos, font_size=10, font_color="white")
        
        plt.title(f"Why recommend User #{top_rec}?", fontsize=12)
        plt.legend(scatterpoints=1)
        plt.axis('off')
        
        st.pyplot(fig)
        st.caption(f"Visualizing the connection between **User {selected_user}** and **User {top_rec}** through their shared friends.")