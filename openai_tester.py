# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import json
client = openai.OpenAI(api_key="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")



response = client.chat.completions.create(
    model="gpt-4",
    messages=[
    {
        "role": "user",
        "content": "give me JUST a number: AVERAGE time spent in grocery store without any extra words. don't say \"the average time spent in a grocery store is\" and don't say “minute”. the unit will be minutes, but only give the number back"
    }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
#print(response.json())
#print(type(response.json()))

jsonified_response=json.loads(response.json())
#print(type(jsonified_response))

print(jsonified_response["choices"][0]["message"]["content"])

#print(json_ed["id"])
#print(response.json()["id"])
