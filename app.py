from os import getenv
from dotenv import load_dotenv
from discord import Message, Client, channel, Intents
from DallEUtil import GenerateImage

load_dotenv()

class MyClient(Client):

    async def on_ready(self):
        print(f'Logged in as {self.user}.')

    async def on_message(self, message: Message):
        if message.reference and not message.is_system() and message.author != self.user and message.content[0] == ';' and len(message.content) < 900:
            try:
                imgURL = GenerateImage(message.content[1:])
            except:
                print('Error encountered during image generation.')
                return
            print('sending message...')
            botmsg = await message.channel.send(f'{imgURL}', reference=message.reference)
            await botmsg.channel.send(f'- {message.author.display_name}', reference=botmsg)
            print('message sent, deleting user message...')
            await message.delete()
            print('user message deleted.')

intents = Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token=getenv('DISCORD_TOKEN'))