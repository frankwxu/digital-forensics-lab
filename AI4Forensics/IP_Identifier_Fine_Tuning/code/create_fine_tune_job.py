import openai

openai.api_key = "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"

# check file id: print(openai.File.list())
file_id = "file-1kZdBPJtBAHOehkHuhc8z5N1"
fine_tune = openai.FineTune.create(training_file=file_id, model="ada")

# Fine tuning job id
print(fine_tune)
