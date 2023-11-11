# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
    {
        "role": "user",
        "content": "hi\n"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?\n"
    },
    {
        "role": "user",
        "content": "give me JUST a number: AVERAGE time spent in grocery store without any extra words. don't say \"the average time spent in a grocery store is\" and don't say “minute”. the unit will be minutes, but only give the number back"
    },
    {
        "role": "assistant",
        "content": "41"
    }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)