# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import jsonify
import json
client = openai.OpenAI(api_key="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")
import readingFronty

#from backend import Task
#x = Task[1].getname()


def processAI(x):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {
            "role": "user",
            "content": f"give me JUST a number: AVERAGE time spent in {x} without any extra words. don't say \"the average time spent in a {x} is\" and don't say “minute”. the unit will be minutes, but only give the number back"
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

    #print(jsonified_response["choices"][0]["message"]["content"])
    return(jsonified_response["choices"][0]["message"]["content"])

    #jsonified_response=json.loads(response.json())
#print(type(jsonified_response))

    #print(["choices"][0]["message"]["content"])

#print(json_ed["id"])
#print(response.json()["id"])
