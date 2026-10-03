import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class OlympusBot(commands.Bot):
    async def setup_hook(self):
        extensions = (
            "cogs.general",
            "cogs.say",
            "cogs.robux_buy",
            "cogs.blox_buy",
            "cogs.auto_mm",
            "cogs.manual_mm",
            "cogs.history",
            "cogs.policies",
        )
        for extension in extensions:
            await self.load_extension(extension)

bot = OlympusBot(command_prefix="$", intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"OLYMPUS online as {bot.user}")

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN is missing. Add it to your host environment.")
bot.run(token)
