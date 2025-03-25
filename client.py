from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)