import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

ALLOWED_GUILD_ID = 1555485039154827274
GUILD = discord.Object(id=ALLOWED_GUILD_ID)

intents = discord.Intents.default()
intents.members = True

class OlympusBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.slash")
        self.tree.copy_global_to(guild=GUILD)
        synced = await self.tree.sync(guild=GUILD)
        print(f"Synced {len(synced)} Olympus slash commands to guild {ALLOWED_GUILD_ID}")

bot = OlympusBot(command_prefix=commands.when_mentioned, intents=intents, help_command=None)

@bot.event
async def on_guild_join(guild):
    if guild.id != ALLOWED_GUILD_ID:
        await guild.leave()

@bot.event
async def on_ready():
    print(f"OLYMPUS online as {bot.user}")

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN is missing. Add it to your host environment.")

bot.run(token)
