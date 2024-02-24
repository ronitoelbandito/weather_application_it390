#Super basic Dall-E engine for making mid images
import os
import openai

PROMPT = "Dall-E prompt goes here"

openai.api_key = "OPEN AI API KEY GOES HERE"

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)

print(response["data"][0]["url"])