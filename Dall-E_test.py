#Dall-E 3 engine for making advanced pictures
import openai

#API KEY
openai.api_key = 'OPEN AI API KEY HERE'

response = openai.Image.create(
    model="dall-e-3",  # Adjust the model name if needed
    prompt="PICTURE PROMPT GOES HERE",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response['data'][0]['url']

print(image_url)
