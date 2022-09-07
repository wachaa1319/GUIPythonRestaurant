import openai
import json

openai.api_key = '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'
def generate(name:str, review:str):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Write a restaurant review based on these notes:\n\nName: {name}\n{review}\n\nReview:",
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    data = json.loads(str(response))
    return data['choices'][0]['text']