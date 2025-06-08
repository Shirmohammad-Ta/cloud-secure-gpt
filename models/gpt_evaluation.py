
import pandas as pd

df = pd.read_csv("data/threat_to_technique_dataset.csv")

few_shot_prompt = """Suggest the best cloud security technique for each threat below:

Threat: Phishing attack
Technique: Identity-Based Authentication (IBA)

Threat: Denial of service
Technique: Self-Cleansing Intrusion Tolerance (C-SCIT)

Threat: Password Guessing
Technique: Role-Based Access Control (RBAC)

Threat: Injection attack
Technique:
"""

print("Example few-shot prompt to test in GPT:")
print(few_shot_prompt.strip())
print("\nTo test, copy this prompt into ChatGPT or OpenAI Playground.")
