from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=getenv('OPENAI_KEY'))

def GenerateImage(prompt: str):
    print(f'Generating image with prompt: {prompt}.')
    response = client.images.generate(
        model='dall-e-2',
        prompt= 'twitch emote style, ' + prompt,
        size="256x256",
        quality="standard",
        n=1
    )
    print('Finished image generation.')

    return response.data[0].url