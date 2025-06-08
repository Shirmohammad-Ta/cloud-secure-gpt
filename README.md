# cloud-secure-gpt
A hybrid system using RoBERTa and GPT for analyzing cloud computing threats and recommending mitigation techniques.


# 🔐 Cloud Threat Mitigation with LLMs (GPT + RoBERTa)

This repository accompanies the paper **"Enhancing Cloud Security using LLMs: A Hybrid Analysis of Challenges and AI-Powered Mitigation"**, which explores a novel approach to understanding and mitigating cloud security threats using traditional classification methods and large language models.

---

## 📌 Project Overview

The project consists of two main components:

1. **Threat Classification**  
   Using RoBERTa for multi-label classification of cloud security threats based on their impact on attributes like confidentiality, integrity, and availability.

2. **Threat-Mitigation Recommendation**  
   Leveraging GPT via prompt engineering to recommend appropriate mitigation techniques for each threat.

---

## 📂 Repository Structure

```bash
cloud-secure-gpt/
│
├── data/                        # 📊 Datasets
│   ├── cloud_security_challenges.csv
│   ├── cloud_security_techniques.csv
│   ├── threat_to_technique_dataset.csv
│   └── threat_to_technique_dataset.jsonl
│
├── notebooks/                  # 🧠 Jupyter notebooks
│   ├── roberta_training.ipynb
│   └── gpt_prompt_test.ipynb
│
├── results/                    # 📈 Output charts and tables
│   ├── results_roberta_accuracy.png
│   ├── results_gpt_match_summary.png
│   └── results_gpt_vs_real.csv
│
├── models/                     # ⚙️ Python scripts for training and evaluation
│   ├── train_roberta.py
│   └── gpt_evaluation.py
│
├── paper/                      # 📄 Paper draft (optional)
│   └── final_paper.pdf
│
├── LICENSE
└── README.md


## 📊 Datasets

All datasets were derived from structured security challenge and technique tables (Appendix A and B in the paper):

- `cloud_security_challenges.csv`: Multi-label annotations for 40+ cloud threats.
- `cloud_security_techniques.csv`: Categorized mitigation strategies by impact.
- `threat_to_technique_dataset.csv/jsonl`: Used for training GPT-style mappings.

---

## 🤖 Models

- **RoBERTa**: Used for multi-label classification of threats based on their impact on security attributes.
- **GPT (via Prompting)**: Used to recommend best-fit mitigation techniques for each threat.  
  → See `notebooks/gpt_prompt_test.ipynb` for prompt examples and evaluation.

---

## 📈 Results

- **RoBERTa** achieved ~80% accuracy across major security attributes.
- **GPT** matched ~88% of threat-to-technique mappings (exact or partial matches).
- 📁 See `results/` folder for evaluation charts and comparison tables.

---

## 🧪 Reproducing the Experiments

### 🔹 Train RoBERTa
```bash
cd models/
python train_roberta.py

---

## 🧪 Run GPT Prompt Evaluation

To generate GPT-style prompt templates for threat-to-technique mapping:

```bash
cd models/
python gpt_evaluation.py

Prompts will be saved in:

```bash
results/gpt_prompts.txt


---

## 🛡 License

This project is licensed under the **MIT License**.

```yaml
name: MIT License
url: https://opensource.org/licenses/MIT
permissions:
  - commercial-use
  - modification
  - distribution
  - private-use
limitations:
  - liability
  - warranty
conditions:
  - include-copyright
  - include-license
