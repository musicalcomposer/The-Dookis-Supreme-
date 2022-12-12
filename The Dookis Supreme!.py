import os
import keyboard
import random
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

input(" ")
client = discord.Bot()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print("amogusamogus'd {0.user}".format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    nicknameamogus = str(message.author).split("*")[0]
    channel = str(message.channel.name)
    messageofsussyboi = str(message.content)

    print("hey {nicknameamogus} eat amogus bozo ratio im in {channel}")
    if nicknameamogus == client.user:
        input(" ")
        if nicknameamogus == ["Wrathay", "weath", "wrath", "upside umop's waifu"]:
            input(" ")
            #make code to change status to "oh no weath is here"
            await message.channel.send("weath ur balls are weird also ur carpet balls ballsballs also i have a question is umop hot")
            amog = ["no", "naur", "NAUR", "nope"]
            if message.content.lower(amog):
                input(" ")
                while True:
                    a = input("spam her until she says yes or amogus mode")
                    if a == "spam":
                        input(" ")
                        while True:
                            await message.channel.send("say yes @{nicknameamogus} or ur sus")
                            if message.content.lower("yes"):
                                message.channel.send("uwu")
                                input("")
                    if a == "amogus mode":
                        message.channel.send("youve just been amogus mode'd")
                        input(" ")
                            