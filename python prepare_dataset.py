import pandas as pd

# Read the downloaded dataset (tab separated)
data = pd.read_csv("SMSSpamCollection", sep="\t", names=["label","message"])

# Save it as CSV inside dataset folder
data.to_csv("dataset/spam.csv", index=False)

print("Dataset created successfully!")