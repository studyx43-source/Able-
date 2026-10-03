from discord.ext import commands
from utils.embeds import olympus_embed

class General(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def help(self, ctx):
        e = olympus_embed("HELP", "Olympus uses separate panels for every service.")
        e.add_field(name="Marketplace", value="$buyrobux\n$buyfruit", inline=True)
        e.add_field(name="Middleman", value="$automm\n$manualmm", inline=True)
        e.add_field(name="Information", value="$rules\n$tos\n$privacy\n$history\n$transaction", inline=False)
        await ctx.send(embed=e)

async def setup(bot): await bot.add_cog(General(bot))
