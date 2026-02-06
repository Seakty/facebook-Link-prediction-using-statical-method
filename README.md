# 🔗 Facebook Link Prediction Using Statistical Methods

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**A Graph-Based Machine Learning Project for Social Network Link Prediction**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Project Structure](#project-structure) • [Results](#results)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Key Algorithms](#key-algorithms)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project leverages **Graph Theory** and **Statistical Methods** to predict missing links in social networks. Using the Facebook Ego Networks dataset, the system applies the **Adamic-Adar Index** algorithm to recommend potential connections (people you may know) with high accuracy.

### 📊 Key Metrics
- **Dataset**: Facebook Ego Networks (facebook_combined.txt)
- **Approach**: Link Prediction using Topological Features
- **Primary Algorithm**: Adamic-Adar Index
- **Interactive Interface**: Streamlit Dashboard

---

## ✨ Features

- 🔮 **Smart Link Prediction**: Uses Adamic-Adar algorithm to predict potential social connections
- 📊 **Interactive Dashboard**: Real-time visualization and recommendations using Streamlit
- 🕸️ **Network Visualization**: Beautiful graph visualizations of user connections
- 👥 **Mutual Friends Analysis**: Displays mutual connections and shared networks
- ⚡ **Fast Scoring**: Optimized candidate filtering for efficient computation
- 📈 **Comprehensive Metrics**: User stats, connection counts, and scoring details

---

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone git@github.com:Seakty/facebook-Link-prediction-using-statical-method.git
cd facebook-Link-prediction-using-statical-method
```

### Step 2: Install Dependencies

Using `uv` (recommended for speed):
```bash
uv sync
```

Or using `pip`:
```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python --version
```

---

## 📁 Project Structure

```
facebook-Link-prediction-using-statical-method/
│
├── 📄 app.py                          # Main Streamlit dashboard application
├── 📄 main.py                         # Data processing and graph creation
├── 📊 facebook_combined.txt           # Facebook Ego Networks dataset
├── 💾 graph_data.pkl                  # Pre-processed graph (NetworkX format)
│
├── 📋 pyproject.toml                  # Project configuration
├── 🔒 uv.lock                         # Dependency lock file
├── 📚 README.md                       # This file
├── 📝 .gitignore                      # Git ignore rules
│
└── 📦 .python-version                 # Python version specification
```

---

## 🎮 Usage

### Option 1: Run the Interactive Dashboard (Recommended)

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

**Dashboard Features:**
- 🔍 Select any user from the network
- 🎯 Choose number of recommendations (1-10)
- 📊 View top recommendations with scores
- 🕸️ Visualize the relationship network

### Option 2: Run Data Processing

To regenerate the graph from raw data:

```bash
python main.py
```

This will:
1. Load `facebook_combined.txt`
2. Create a NetworkX graph
3. Save it as `graph_data.pkl`

---

## 🧠 Key Algorithms

### Adamic-Adar Index

The Adamic-Adar Index predicts links based on shared neighbors:

$$\text{AA}(x, y) = \sum_{z \in N(x) \cap N(y)} \frac{1}{\log(|N(z)|)}$$

Where:
- **N(x)**: Set of neighbors of node x
- **N(y)**: Set of neighbors of node y
- The index gives more weight to mutual friends with fewer connections

### Why This Works?

✅ Users are more likely to connect if they have mutual friends  
✅ Common friends with niche interests are more valuable signals  
✅ Computationally efficient for large networks  

---

## 📊 Results

### Recommendation Metrics

| Metric | Value |
|--------|-------|
| **Nodes (Users)** | 4,039 |
| **Edges (Friendships)** | 88,234 |
| **Average Degree** | 43.7 |
| **Network Density** | ~0.01 |
| **Connected Components** | 1 |

### Example Output

```
User #1 Recommendations:
┌───────┬─────────┬───────────┬─────────────────┐
│ Rank  │ User ID │   Score   │ Mutual Friends  │
├───────┼─────────┼───────────┼─────────────────┤
│  1    │   456   │   2.847   │      12         │
│  2    │   789   │   2.156   │       8         │
│  3    │   234   │   1.943   │       7         │
└───────┴─────────┴───────────┴─────────────────┘
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **NetworkX** | Graph creation and analysis |
| **Streamlit** | Interactive web dashboard |
| **Pandas** | Data manipulation |
| **Matplotlib** | Network visualization |
| **Python** | Core programming language |

---

## 📚 Dataset Information

**Facebook Ego Networks Dataset:**
- **Source**: Stanford Large Network Dataset Collection
- **Format**: Undirected, unweighted graph
- **Size**: 4,039 nodes, 88,234 edges
- **Description**: Subgraph of Facebook friend network

---

## 🎓 Educational Value

This project demonstrates:
- ✅ Graph Theory fundamentals
- ✅ Link prediction techniques
- ✅ Network analysis and visualization
- ✅ Streamlit app development
- ✅ Data processing pipelines
- ✅ Scientific computing with Python

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact & Support

For questions or support regarding this project:
- 📌 **GitHub**: [Seakty](https://github.com/Seakty)
- 💬 **Issues**: Open an issue on the GitHub repository

---

## 🙏 Acknowledgments

- **Stanford SNAP** for the Facebook Ego Networks dataset
- **NetworkX** community for excellent graph tools
- **Streamlit** for the interactive dashboard framework

---

<div align="center">

**Made with ❤️ for Graph Theory & Data Science**

⭐ If you found this project helpful, please consider starring it!

</div>
