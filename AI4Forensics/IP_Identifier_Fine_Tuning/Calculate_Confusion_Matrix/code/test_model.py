import openai
import project_keys
import os
import pandas as pd
import time

start_time = time.time()

openai.api_key = project_keys.key

FINE_TUNED_MODEL = "ada:ft-personal-2023-10-09-15-25-25"

# Prompt
data = pd.read_csv("testing100_dataset.csv")

YOUR_PROMPT = []
for i in range(len(data)):
    # prompt consists of text and IP recoginzed by regular expression
    YOUR_PROMPT.append(f"{data.iloc[i,0]} | {data.iloc[i,1]}")

def get_completion(prompt, max_token):
    return openai.Completion.create(
        model=FINE_TUNED_MODEL, max_tokens=max_token, prompt=prompt, temperature=0.1
    ).choices[0]["text"]


if type(YOUR_PROMPT) is not str:
    result = []
    # with open(YOUR_PROMPT, "r") as file:
    for prompt_index in range(len(YOUR_PROMPT)):
        # i += 1
        prompt = YOUR_PROMPT[prompt_index] + " ->"  # Index of prompt
        try:
            result.append(get_completion(prompt, 1))
        except openai.error.InvalidRequestError as e:
            print(f"Caught an InvalidRequestError on prompt {prompt_index}: {str(e)}")

    print(result)
    df = pd.DataFrame(columns=["pred_label"], data=result)

    data_ai = pd.concat([data, df], axis=1)
    data_ai.to_csv(
        "testing100_results_dataset.csv", index=False
    )
    print(result)

else:
    result = get_completion(YOUR_PROMPT, 8)
    print(f"\n{result}")


elapsed_time = time.time() - start_time
print("\nExecution time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
