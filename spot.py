import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot ready")

@client.event
async def on_command_error(ctx, error):
    pass

@client.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')

client.run('NzI3MDI2OTEwNTI5NDU0MTMw.Xvl3Dg.RIvEPekWRpSYqyQ8yY08HIs8FCE')