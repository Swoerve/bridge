import discord
import os # default module
from dotenv import load_dotenv
from aiohttp import ClientSession

load_dotenv() # load all the variables from the env file

intents = discord.Intents(messages=True, guilds=True)
intents.reactions = True
intents.message_content = True

bot = discord.Bot(intents=intents)

wb_url_jsu24 = "https://discord.com/api/webhooks/1286643148050796626/KxSW9c8FfibD5Ug5-iC71kjN_Cukrl9VW6IWYYSNPUFLnxmhNq7dxiu2D_NCjtPJLN1r"
wb_url_feu24 = "https://discord.com/api/webhooks/1286645423393472607/TQ9f0anmU9KwSc-GULslCD9GIq-eizcUbQwvu_MxlqshBXkzXZURUjM3rownR0UrSPaK"

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message: discord.Message):
    async with ClientSession() as session:
        if not message.author.bot:
            
            chn1 = bot.get_channel(1137065839636533268)
            chnjsu = bot.get_channel(1286639089583656960)
            if message.channel.id == 1137065839636533268:
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

            if message.channel.id == 1286639089583656960:
                print(message.content + ", " + message.author.name + ", " + str(message.channel.id))
                #await chn1.send(message.author.name + ": " + message.content)
                webhook = discord.Webhook.from_url(wb_url_feu24, session=session)
                await webhook.send(content=message.content, username=message.author.display_name, avatar_url=message.author.display_avatar)

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token
