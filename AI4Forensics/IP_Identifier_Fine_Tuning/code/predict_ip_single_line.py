import openai

openai.api_key = "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"

FINE_TUNED_MODEL = "ada:ft-university-of-baltimore-2023-08-14-12-39-06"

# take one positive and one negative sample from dataset_test.jsonl
prompt_neg = "\t<string>3608.80.24.1.8</string>;608.80.24.1 ->"
prompt_pos = "\t<string>2.20.31.4</string>;2.20.31.4 ->"


def get_completion(prompt, max_token):
    return openai.Completion.create(
        model=FINE_TUNED_MODEL, max_tokens=max_token, prompt=prompt
    ).choices[0]["text"]


# 1 means 1 token
print(f"The truth:'Negative', the predition: '{get_completion(prompt_neg, 1)}'")
print(f"The truth:'Positive', the predition: '{get_completion(prompt_pos, 1)}'")
