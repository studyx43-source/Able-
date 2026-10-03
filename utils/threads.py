import discord

async def create_private_thread(message: discord.Message, name: str, users=None):
    thread = await message.create_thread(name=name, type=discord.ChannelType.private_thread)
    for user in users or []:
        await thread.add_user(user)
    return thread
