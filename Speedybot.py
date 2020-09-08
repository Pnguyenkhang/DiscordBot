import discord 
import random

from discord.ext import commands

# instance of a bot created
# If change variable bot then the @ decorators variabbles must change to bot as well
client = commands.Bot(command_prefix = '!')

@client.event 
async def on_ready():
    print('Speedy Bot is online!')


@client.command() # ctx is content passed in automatically
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms') # when command is run, bot will print



@client.event # piece of code that is triggered when user tells bot to trigger
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')



# deletes latest messages with the clear command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount) #Accessing channel that command was running and deleting messages

client.run('NzI3Mjg3MjQ4Njk3MTYzNzk3.Xvpppg.QQnu7_ht_uk6Ky_EOsse-ePW_IY')