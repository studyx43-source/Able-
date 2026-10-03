from discord.ext import commands
from utils.embeds import olympus_embed

class Say(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, text: str):
        await ctx.message.delete()
        await ctx.send(embed=olympus_embed("ANNOUNCEMENT", text))

async def setup(bot): await bot.add_cog(Say(bot))
