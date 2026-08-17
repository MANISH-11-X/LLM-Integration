from groq import Groq #groq is a python library that allows your python program to communicate with groq api
from dotenv import load_dotenv #it allows to read variables from your .env file
import os #os module is used to access env variables.

load_dotenv() #read the env file and load its variable

client = Groq(
    api_key=os.getenv("GROQ_API_KEY") #after load_dotenv() python can access api key
)

question = input("Enter Your Question:")

response = client.chat.completions.create( #it tells the groq create an ai response for me.
    model="openai/gpt-oss-120b",
    messages =[
        {
            "role":"user", #This msg came from user.
            "content":question
        }
    ]
)

'''
openai/gpt-oss-120b
meta-llama/llama-prompt-guard-2-22m
openai/gpt-oss-safeguard-20b
groq/compound
whisper-large-v3-turbo
meta-llama/llama-prompt-guard-2-86m
allam-2-7b
whisper-large-v3
canopylabs/orpheus-v1-english
qwen/qwen3.6-27b
canopylabs/orpheus-arabic-saudi
groq/compound-mini
openai/gpt-oss-20b
'''

answer = response.choices[0].message.content #response = comple response from the api, choices[0] give me the first choices(response), in the form of msg.
print("AI", answer)
