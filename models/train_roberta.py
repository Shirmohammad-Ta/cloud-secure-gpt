
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import Dataset

class ThreatDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=64):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        inputs = self.tokenizer(
            self.texts[idx], padding='max_length', truncation=True,
            max_length=self.max_len, return_tensors="pt"
        )
        inputs = {k: v.squeeze(0) for k, v in inputs.items()}
        inputs['labels'] = torch.tensor(self.labels[idx], dtype=torch.float)
        return inputs

# Load data
df = pd.read_csv("data/cloud_security_challenges.csv")
X = df["Challenge"].tolist()
y = df.drop(columns=["Challenge"]).values.tolist()
labels = df.columns[1:].tolist()

# Tokenizer
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

# Prepare datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
train_dataset = ThreatDataset(X_train, y_train, tokenizer)
test_dataset = ThreatDataset(X_test, y_test, tokenizer)

# Load model
model = RobertaForSequenceClassification.from_pretrained(
    "roberta-base", num_labels=len(labels), problem_type="multi_label_classification"
)

# Train
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=10
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

trainer.train()
