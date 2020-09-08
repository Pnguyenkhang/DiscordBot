
# Exit Constants
EXIT_FAILURE = 1
EXIT_SUCCESS = 0

# IMPORT ERROR CHECKER
try:
    import discord
except ImportError as importError:
    print(importError)
    exit(EXIT_FAILURE)

try:
    import random
except ImportError as importError:
    print(importError)
    exit(EXIT_FAILURE)

try:
    from discord.ext import commands, tasks
except ImportError as importError:
    print(importError)
    exit(EXIT_FAILURE)

try:
    import os
except ImportError as importError:
    print(importError)
    exit(EXIT_FAILURE)

try:
    from itertools import cycle
except ImportError as importError:
    print(importError)
    exit(EXIT_FAILURE)



# instance of a bot created
# If change variable bot then the @ decorators variabbles must change to bot as well
client = commands.Bot(command_prefix = '.')
status = cycle(['Hello there!','Enjoy your stay!, I am becoming self aware!'])

@client.event 
async def on_ready():
    change_status.start()
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('I am becoming aware!'))
    print('Bot is ready')

@tasks.loop(seconds=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(aliases = ['8ball', 'test']) # can invoke using either or
async def _8ball(ctx, *, question): # context, question mark, asterisk allows me to take in multiple paramaters
    responses = ['no',
    'yes',
    'maybe',
    'never',
    'absolutely never',
    'definite yes']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases = ['outtahere'])
async def kick(ctx, member : discord.Member, *, reason=None): # read in member as member object
    await member.kick(reason=reason)

@client.command(aliases = ['gone'])
async def ban(ctx, member : discord.Member, *, reason=None): # read in member as member object
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def unban(ctx, *, member): # for accounts with spaces in between the name
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator)==(member_name, member_discriminator): # creates tuple
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension has loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension has loaded')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension has reloaded')

# Client events
@client.event # piece of code that is triggered when user tells bot to trigger
async def on_member_join(member):
    print(f'{member} has joined a server.')

def is_it_me(ctx):
    return ctx.author.id == 315606293693857793

@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used!')


# deletes latest messages with the clear command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount) #Accessing channel that command was running and deleting messages


@clear.error # Must be below purge command
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')


# go through all files in cog n load py files
for filename in os.listdir('./cogs'): # works with all .py files
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(filename[:-3])

client.run('NzI3MDI2OTEwNTI5NDU0MTMw.Xvl3Dg.RIvEPekWRpSYqyQ8yY08HIs8FCE')