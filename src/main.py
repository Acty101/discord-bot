import discord
import os
import requests
from enum import Enum
from dotenv import load_dotenv

# env vars
load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")


class Commands(Enum):
    HELP = "help"


class MyClient(discord.Client):
    TMP_DIR = "./tmp/"

    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # only call bot functions on !
        if message.content.startswith("!"):
            cmd = message.content[1:]
            match cmd:
                case Commands.HELP.value:
                    await self._print_help(message)
        # if any attachements detected on message
        if message.attachments:
            # want to download msg into /tmp folder -> run face_recognition and return results
            attachments = message.attachments
            for attachment in attachments:
                url = attachment.url
                filename = attachment.filename
                data = {"url": url, "filename": filename}
                response = requests.post(f'http://face_rec_model:8000/lipstick', json=data)
                if response.status_code == 200:
                    image_data = response.content
                    img_path = os.path.join(self.TMP_DIR, "response_img.jpg")
                    if not os.path.exists(self.TMP_DIR):
                        os.mkdir(self.TMP_DIR)
                    with open(img_path, 'wb') as file:
                        file.write(image_data)
                    await message.channel.send(file=discord.File(fp=img_path, filename="lipped.jpg"))
                    
                else:
                    print(f"Error displaying image")
                


    async def _print_help(self, message):
        await message.channel.send(
            f"Usage: [! <command>]\nList of available commands:\n1. help"
        )


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
