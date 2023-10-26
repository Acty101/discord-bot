import discord
import os
from enum import Enum
from dotenv import load_dotenv

# env vars
load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")


class Commands(Enum):
    HELP = "help"


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # only call bot on !
        if message.content.startswith("!"):
            cmd = message.content[1:]
            match cmd:
                case Commands.HELP.value:
                    await self._print_help(message)

    async def _print_help(self, message):
        await message.channel.send(
            f"Usage: [! <command>]\nList of available commands:\n1. help"
        )


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
