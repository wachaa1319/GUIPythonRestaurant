import os
import openai
import json

openai.api_key = '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'

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Write a restaurant review based on these notes:\n\nName: The Blue Wharf\nLobster great, noisy, service polite, prices good.\n\nReview:",
  temperature=0.5,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

data = json.loads(str(response))
print(data['choices'][0]['text'])