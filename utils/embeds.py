import discord

def olympus_embed(title: str, description: str | None = None) -> discord.Embed:
    embed = discord.Embed(title=f"OLYMPUS\n{title}", description=description)
    embed.set_footer(text="Olympus Middleman & Marketplace")
    return embed
