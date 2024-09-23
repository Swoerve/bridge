import discord
import os # default module
from dotenv import load_dotenv
from aiohttp import ClientSession

load_dotenv() # load all the variables from the env file


# Set up discord bot intents
intents = discord.Intents(messages=True, guilds=True)
intents.reactions = True
intents.message_content = True

# Initialize bot object
bot = discord.Bot(intents=intents)


# Get the webhooks from env
wb_url_jsu24 = str(os.getenv("WH-JSU24"))
wb_url_feu24 = str(os.getenv("WH-FEU24"))
ch_jsu24 = int(os.getenv("CH-JSU24"))
ch_feu24 = int(os.getenv("CH-FEU24"))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message: discord.Message):
    async with ClientSession() as session:
        if not message.author.bot:
            
            chnjsu = bot.get_channel(ch_jsu24)
            chnfeu = bot.get_channel(ch_feu24)
            if message.channel.id == ch_feu24:
                print(message.content + ", " + message.author.name + ", " + str(message.channel.id))
                #await chnjsu.send(message.author.name + ": " + message.content)
                webhook = discord.Webhook.from_url(wb_url_jsu24, session=session)
                if len(message.attachments) > 0:
                    newcontent = ""
                    newcontent += message.content
                    for i in message.attachments:
                        newcontent += i.url
                        newcontent += " "
                    await webhook.send(content=newcontent, username=message.author.display_name, avatar_url=message.author.display_avatar)
                else:
                    await webhook.send(content=message.content, username=message.author.display_name, avatar_url=message.author.display_avatar)

            if message.channel.id == ch_jsu24:
                print(message.content + ", " + message.author.name + ", " + str(message.channel.id))
                #await chn1.send(message.author.name + ": " + message.content)
                webhook = discord.Webhook.from_url(wb_url_feu24, session=session)
                if len(message.attachments) > 0:
                    newcontent = ""
                    newcontent += message.content
                    for i in message.attachments:
                        newcontent += i.url
                        newcontent += " "
                    await webhook.send(content=newcontent, username=message.author.display_name, avatar_url=message.author.display_avatar)
                else:
                    await webhook.send(content=message.content, username=message.author.display_name, avatar_url=message.author.display_avatar)


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token
