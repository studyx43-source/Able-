import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = 1555485039154827274
GUILD = discord.Object(id=GUILD_ID)

class OlympusBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned, intents=discord.Intents.default(), help_command=None)

    async def setup_hook(self):
        await self.load_extension("cogs.policies")
        synced = await self.tree.sync(guild=GUILD)
        print(f"Synced {len(synced)} command(s)")

bot = OlympusBot()

@bot.event
async def on_ready():
    print(f"OLYMPUS online as {bot.user}")

@bot.event
async def on_guild_join(guild):
    if guild.id != GUILD_ID:
        await guild.leave()

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN is missing.")
bot.run(token)
