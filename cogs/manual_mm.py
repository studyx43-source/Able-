import discord
from discord.ext import commands
from utils.embeds import olympus_embed

class ManualMMView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Request Middleman", style=discord.ButtonStyle.primary, custom_id="olympus:manualmm:create")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Your Manual Middleman request has been started.", ephemeral=True)

class ManualMM(commands.Cog):
    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def manualmm(self, ctx):
        await ctx.send(embed=olympus_embed("MANUAL MIDDLEMAN", "Request a human-assisted middleman transaction."), view=ManualMMView())

async def setup(bot):
    bot.add_view(ManualMMView())
    await bot.add_cog(ManualMM(bot))
