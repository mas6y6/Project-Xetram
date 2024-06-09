import discord.ext
import discord.ext.commands
from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.api.client import XboxLiveClient
import random

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your bot's token
DISCORD_TOKEN = open("token.txt").readline()
XBOX_TOKEN = open("token.txt").readline()
# Initialize the Discord bot

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.ext.commands.Bot(command_prefix='!', intents=intents)
connectionsdm = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

async def discordconnectionhandler(user: discord.User):
    #await user.send()
    

async def discordconnectionstarter(message: discord.Message):
    con = message.content
    try:
        connectionsdm[message.author.id]
    except:
        print("Starting New connection")
        xuser = None
        dmdiscord = bot.get_user(message.author.id).create_dm()
        connectionsdm[message.author.id] = {"auth":False,"xboxuser":xuser,"authid":random.randint(10000000,99999999),"dm":dmdiscord,"stats":{}}
        print(connectionsdm[message.author.id])
        
    else:
        await discordconnectionhandler(bot.get_user(message.author.id))

@bot.event
async def on_message(message: discord.Message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Log the message content
    print(f'{message.author.name}: {message.content}')

    # Reply to the message in the same channel
    if int(message.channel.id) == 1248709021112995890:
        await bot.process_commands(message)
    elif type(message.channel) == discord.channel.DMChannel:
        await discordconnectionstarter(message)

@bot.command(name='dm')
async def dm(ctx: discord.ext.commands.Context):
    user_id = ctx.author.id
    user = await bot.fetch_user(user_id)
    ctx.reply("A new Xbox chat connection DM has been opened")
    user_id = ctx.author.id
    user = await bot.fetch_user(user_id)
    await user.send("Please text their Xbox Gamertag or their XUID if possible(You can get their XUID using https://cxkes.me/xbox/xuid)")

# Run the Discord bot
bot.run(DISCORD_TOKEN)
