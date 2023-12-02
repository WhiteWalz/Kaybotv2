from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=getenv('OPENAI_KEY'))

def GenerateImage(prompt: str):
    print(f'Generating image with prompt: {prompt}.')
    response = client.images.generate(
        model='dall-e-3',
        prompt= prompt + ', in the style of a twitch emote',
        size="1024x1024",
        quality="standard",
        n=1
    )
    print('Finished image generation.')

    return response.data[0].url