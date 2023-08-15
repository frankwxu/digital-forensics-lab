import pandas as pd
import json
import os


# Read the CSV file into a DataFrame
file_path = os.path.join(os.getcwd(), "./openAI/dataset_small.csv")

data = pd.read_csv(file_path)

# Create a list to store the converted data
json_list = []

# Iterate through each row and create the JSON format
for index, row in data.iterrows():
    prompt_text = (
        row["text"] + ";" + row["ip"] + " ->"
    )  # Replace with the actual column name for "promote" text
    completion_text = (
        " positive" if row["class"] != "N" else " negative"
    )  # Replace with the actual column name for "completion" text

    # Create a dictionary for the JSON object
    json_object = {"prompt": prompt_text, "completion": completion_text}

    json_list.append(json_object)

# Write the converted data to a JSON file
output_file_path = os.path.join(
    os.getcwd(), "./openAI/dataset_small.json"
)  # Replace with the desired output file path


# Calculate the split index
split_index = int(0.8 * len(json_list))

# Split the list into two parts
train_data = json_list[:split_index]
test_data = json_list[split_index:]

# File paths for train and test data
train_file_path = os.path.join(os.getcwd(), "./openAI/dataset_train.jsonl")
test_file_path = os.path.join(os.getcwd(), "./openAI/dataset_test.jsonl")

# Write train data to file
with open(train_file_path, "w") as train_file:
    for json_object in train_data:
        line = json.dumps(json_object) + "\n"
        train_file.write(line)

# Write test data to file
with open(test_file_path, "w") as test_file:
    for json_object in test_data:
        line = json.dumps(json_object) + "\n"
        test_file.write(line)

print(
    "JSON objects have been split (80% \and 20%) and written to train_data.jsonl and test_data.jsonl"
)
