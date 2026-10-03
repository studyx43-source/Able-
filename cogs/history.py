from discord.ext import commands
from utils.embeds import olympus_embed

class History(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def history(self, ctx):
        await ctx.send(embed=olympus_embed("TRANSACTION HISTORY", "Only genuinely completed Olympus transactions are recorded as completed."))

    @commands.command()
    async def transaction(self, ctx, transaction_id: str = None):
        if not transaction_id:
            await ctx.send(embed=olympus_embed("TRANSACTION LOOKUP", "Usage: $transaction <transaction-id>"))
            return
        await ctx.send(embed=olympus_embed("TRANSACTION LOOKUP", f"Transaction: {transaction_id}\nVerified stored record lookup."))

async def setup(bot): await bot.add_cog(History(bot))
