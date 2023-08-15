import os
import openai

openai.api_key = "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"

# Path to training data
training_dataset = "./openAI/dataset_train.jsonl"

# Upload file to openai
upload = openai.File.create(file=open(training_dataset, "rb"), purpose="fine-tune")

# Get file id
print(upload["id"])
