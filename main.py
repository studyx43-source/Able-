import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

ALLOWED_GUILD_ID = 1555485039154827274

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

@bot.check
async def guild_only(ctx):
    return ctx.guild is not None and ctx.guild.id == ALLOWED_GUILD_ID

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
