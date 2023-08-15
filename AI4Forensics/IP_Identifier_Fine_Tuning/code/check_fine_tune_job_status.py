import openai

openai.api_key = "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"

fine_tune_job_id = "ft-3DA3kW5k0BaHoWqwjJUB6Xwf"

# Retrieve fine-tuning job details
fine_tune_job = openai.FineTune.retrieve(fine_tune_job_id)

# Check status and other information
print("Fine-tuned Model: " + fine_tune_job.fine_tuned_model)
print("Status: " + fine_tune_job.status)
print("Job Results: ========")
print(fine_tune_job.result_files)
