import discord
from discord.ext import commands
from utils.embeds import olympus_embed

class BloxView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Purchase Blox Fruits", style=discord.ButtonStyle.primary, custom_id="olympus:blox:purchase")
    async def purchase(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Your Blox Fruits purchase request has been started.", ephemeral=True)

class BloxBuy(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def buyfruit(self, ctx):
        await ctx.send(embed=olympus_embed("BLOX FRUITS MARKET", "Purchase available Blox Fruits stock through Olympus."), view=BloxView())

async def setup(bot):
    bot.add_view(BloxView())
    await bot.add_cog(BloxBuy(bot))
