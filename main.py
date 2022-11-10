import os
import discord
import http.client
import requests
import json
import asyncio
import os
from discord.ext import commands
import random
intents = discord.Intents.all()
helpCommand=commands.DefaultHelpCommand(no_category='Commands')
bot=commands.Bot(command_prefix='!ZR',intents=intents, helpCommand=helpCommand)
@bot.event
async def on_connect():
  print("your bot is online")
  
@bot.command()
async def name(ctx,name):
  await ctx.reply("Hello, "+name+" nice to meet you")
@bot.command(brief="This api gives you original jokes to tell your friend and get made fun of")
async def joke(ctx):
  url="https://official-joke-api.appspot.com/random_joke"
  req=requests.get(url)
  data=req.json()
  setup=data["setup"]
  punchline=data["punchline"]
  await ctx.send(setup)
  await asyncio.sleep(3)
  await ctx.send(punchline)

  
@bot.command(brief="This API gives you a random thing to do to get you off your btt and get going.")
async def bored(ctx):
  url="https://www.boredapi.com/api/activity?participants=1"
  req=requests.get(url)
  data=req.json()
  activity=data["activity"]
  type=data["type"]
  link=data["link"]
  await ctx.reply(activity+", type of activity "+type)
  if link.lower()=="":
    await ctx.reply("no link")
  else:
    await ctx.reply(link)




@bot.command(brief="This is the link to show how this program works and the abbreviations of all the suppoerted languages https://rapidapi.com/googlecloud/api/google-translate1/details")
async def translate(ctx,language,translate):  
  url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
  payload = "q="+translate+"&target="+language+"&source=en"
  headers = {
  	"content-type": "application/x-www-form-urlencoded",
  	"Accept-Encoding": "application/gzip",
  	"X-RapidAPI-Key": "f6677d9f63msh8704357c490f518p1fa0aajsn2c6357462b5c",
  	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
  }
  response = requests.request("POST", url, data=payload, headers=headers)
  data = response.json()
  await ctx.reply(translate+" in english is "+data["data"]["translations"][0]["translatedText"])


my_secret = os.environ['token']
bot.run(my_secret)