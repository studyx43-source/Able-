import discord
from discord.ext import commands
from utils.embeds import olympus_embed

class RobuxView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Purchase Robux", style=discord.ButtonStyle.primary, custom_id="olympus:robux:purchase")
    async def purchase(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Your Robux purchase request has been started.", ephemeral=True)

class RobuxBuy(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def buyrobux(self, ctx):
        e = olympus_embed("ROBUX PURCHASE", "Purchase Robux through Olympus. Pricing and payment details are confirmed before payment.")
        await ctx.send(embed=e, view=RobuxView())

async def setup(bot):
    bot.add_view(RobuxView())
    await bot.add_cog(RobuxBuy(bot))
