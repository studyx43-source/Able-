import discord
from discord.ext import commands
from utils.embeds import olympus_embed

class AutoMMView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Create Auto Middleman", style=discord.ButtonStyle.primary, custom_id="olympus:automm:create")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Your Auto Middleman request has been started.", ephemeral=True)

class AutoMM(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def automm(self, ctx):
        await ctx.send(embed=olympus_embed("AUTO MIDDLEMAN", "Create an automated middleman transaction. Both participants must confirm the exact deal terms."), view=AutoMMView())

async def setup(bot):
    bot.add_view(AutoMMView())
    await bot.add_cog(AutoMM(bot))
