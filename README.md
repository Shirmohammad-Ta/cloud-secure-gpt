# Intelligent Cloud Security Framework

A hybrid machine learning and expert knowledge-driven framework for adaptive threat-technique matching in cloud environments. This system combines NLP, large language models, and human expertise to dynamically respond to cloud security threats.

## 🚀 Key Features

- **94.2% accuracy** in threat detection (22.4% improvement over baseline)
- **85ms response time** with 49% reduced resource consumption
- **Adaptive learning** with weekly model updates and parameter auto-tuning
- **Multi-source intelligence** integration (SLR, expert surveys, real-time ML analysis)
- **Explainable AI** with semantic reasoning for decisions

## 📊 Performance Highlights

| Metric | Result | Improvement |
|--------|--------|-------------|
| Overall Accuracy | 94.2% | +22.4% |
| New Attack Detection | 89.5% | +47.2% |
| CPU Usage | 18% | -49% |
| Cost Savings | $250K/year | -62% successful attacks |

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[Threat Description] --> B[NLP Preprocessing]
    B --> C[Semantic Feature Extraction]
    C --> D{Decision Module}
    D --> E[Technique Knowledge Base]
    D --> F[Expert Opinions Database]
    E --> G[Hybrid Optimization]
    F --> G

## 📦 Installation
git clone https://github.com/Shirmohammad-Ta/cloud-secure-gpt.git
cd cloud-secure-gpt
pip install -r requirements.txt

## 🧮 Usage
from threat_matcher import ThreatMatcher

# Initialize the model
matcher = ThreatMatcher()

# Match threat to optimal technique
threat_description = "Attack performed by impersonating system administrator"
optimal_technique, confidence = matcher.match(threat_description)

print(f"Recommended technique: {optimal_technique}")
print(f"Confidence score: {confidence:.3f}")

## 📁 Dataset Structure
data/threat_to_technique.csv: Mapping between threats and mitigation techniques
data/expert_survey_2023.csv: Expert opinions and ratings
data/slr_challenges.csv: Systematic literature review results

## 🎯 Core Algorithms
def match_threat(self, threat_desc: str, alpha=0.6, beta=0.25, gamma=0.15):
    threat_vec = self.model.encode(threat_desc)
    scores = []
    for tech_name, tech_data in self.technique_db.items():
        sim = 1 - cosine(threat_vec, tech_data["vector"])
        adjusted_score = (
            alpha * sim +
            beta * (tech_data["expert_score"] / 10) +
            gamma * torch.exp(-0.1 * tech_data["complexity"])
        )
        scores.append((tech_name, adjusted_score))
    return max(scores, key=lambda x: x[1])

Optimization Parameters
α = 0.6 (semantic similarity weight)
β = 0.25 (expert opinion weight)
γ = 0.15 (complexity penalty weight)
λ = 0.1 (complexity decay factor)

📈 Results Visualization
The repository includes scripts to generate:
Accuracy comparison charts
Resource usage plots
Cost-benefit analysis graphs
Adaptive learning progress curves

📞 Contact
Author: Shirmohammad Tavangari
Email: s.tavangari@alumni.ubc.ca
Institution: University of British Columbia, Canada
GitHub: Shirmohammad-Ta

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
    G --> H[Optimal Technique]
    H --> I[Feedback System]
    I --> C
