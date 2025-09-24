# 1. Install the OpenAI library
# pip install openai

# 2. Import dependencies
from openai import OpenAI
import os

# 3. Configure API key (best practice: from environment variable or config file)
# set your API key in .env or environment
# export OPENAI_API_KEY="your_api_key"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
system → Model ko instruction dena (tum kaise behave karna chahte ho).
Example: “Tum ek helpful assistant ho.”
user → Human ka input / sawaal.
Example: “Who won the world series in 2020?”
assistant → Model ka jawab.
Example: “Los Angeles Dodgers won in 2020.”
system → user → assistant → user → assistant …
//for all
print(response)
//for specific
print(response.choices[0].message.content)
//API key:
Don’t hardcode it in your script.
Put it in .env or config.json and load securely.
Secret Key: You need to generate it from OpenAI dashboard
If you don’t have billing info, it won’t work for production.
Image Recognition:
For images, you’d use client.images.generate() or client.chat.completions.create() with "image_url" content.
User → API → Model → Response)
