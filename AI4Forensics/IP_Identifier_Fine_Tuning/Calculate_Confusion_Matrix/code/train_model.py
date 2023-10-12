import os
import openai
import project_keys
import subprocess

openai.api_key = project_keys.key

# Path to training data
training_dataset = "training400_dataset.jsonl"

# Upload file to openai
upload = openai.File.create(file=open(training_dataset, "rb"), purpose="fine-tune")
validation_upload = openai.File.create(
    file=open(training_dataset, "rb"), purpose="fine-tune"
)

# Get file id
file_id = upload["id"]
validation_id = validation_upload["id"]

fine_tune = openai.FineTune.create(training_file=file_id, model="ada")

# Fine tuning job id
job_id = fine_tune["id"]
# print(f"The Job id is {job_id}")
command = f"openai api fine_tunes.follow -i {job_id}"
completed_process = subprocess.run(
    command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

print(completed_process.stdout)
