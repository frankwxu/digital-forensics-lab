import openai

openai.api_key = "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"

# Returns the contents of the specified file
content = openai.File.download("file-ngHRotibSy82Mr55IjsPP2uK")

# Save content to a local file

file_name = "./openAI/fine_tune_steps.txt"  # Change to the desired file name
with open(file_name, "wb") as f:
    f.write(content)

print(f"File '{file_name}' saved successfully.")
