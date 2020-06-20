import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
@client.command()
async def message(ctx, arg):
    channel = client.get_channel('A channel id') #Channel id's datatype is an int, not a string!
    await channel.send(arg)

client.run('Haha no')
