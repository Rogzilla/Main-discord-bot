import discord
import requests
import json
import asyncio
import os
from discord.ext import commands
import random
intents = discord.Intents.all()
bot=commands.Bot(command_prefix='!Z',intents=intents)
imglist=["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c8b3042e-9399-4832-95c9-c75c76c98d71/dc7axa0-6ab47786-89c5-4bd5-bdf3-c82da4addc3b.jpg/v1/fit/w_375,h_228,q_70,strp/tacocat_and_purrito_by_firestarninja_dc7axa0-375w.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjIyIiwicGF0aCI6IlwvZlwvYzhiMzA0MmUtOTM5OS00ODMyLTk1YzktYzc1Yzc2Yzk4ZDcxXC9kYzdheGEwLTZhYjQ3Nzg2LTg5YzUtNGJkNS1iZGYzLWM4MmRhNGFkZGMzYi5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.x1YuEDSoVNEj42Jx1qp008Nuf9m3sgwMlbo5LCH8qR0","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7d5pbT55Rgq2_2Kj4ZxScb7tGp3PKYUcqsw&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFDWTiCDgE2PjgAhIZpb7LzVBs9wLwpENRDw&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRka1_oGnbJJMuxD9n-GrfocvRFm0hjRPPc9g&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4OfND_R0yKY_yfZuoLV9rtSxC_Sx8_ChF6Q&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuaZp_7qR0qw_gWFszDpcSV7WpoH_0HEySn4x_ogKZ1Ua8KkNEo6J1IyJRKionjV-TogQ&usqp=CAU", "https://media.tenor.com/i-lmUA2hegIAAAAM/funny-meme-taco-cat.gif","https://cdn140.picsart.com/308291966094211.gif?to=crop&type=webp&r=40x40&q=50"]
balllist=["It is certain"," It is decidedly so","Without a doubt","Yes definitely", "Yes may rely on it"," As I see it, yes","Most likely."," Outlook good.","Yes", "Signs point to yes","Reply hazy, try again"," Ask again later."," Ask again later.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
  
@bot.command()
async def ach(ctx):
  await ctx.reply("Hello from Zachbot, the secret word is Poop")
  
@bot.command()
async def achname(ctx,name):
  await ctx.reply("Hello, "+name+" nice to meet you")
  
my_secret = os.environ['token']
@bot.command()
async def achAdd(ctx,num1,num2):
  sum=int(num1)+int(num2)
  await ctx.reply("The answer is "+str(num1)+"+"+str(num2)+"="+(str(sum)))

@bot.command()
async def achtime(ctx,time,period):
  if period.lower()=="am" and int(time)>=5:
    await ctx.reply("Good moring, it is "+str(time))
  elif period.lower()=="am" and int(time)<=4:
    await ctx.reply("Good night, it is "+str(time))
  elif period.lower()=="pm" and int(time)<=4:
    await ctx.reply("Good afternoon, it is "+str(time))
  elif period.lower()=="pm" and int(time)>=5:
    await ctx.reply("Good night, it is "+str(time))  

@bot.command()
async def achTacocat(ctx):
  num=random.randint(0, 6)
  image=imglist[num]
  await ctx.reply(image)
  
@bot.command()
async def ach8Ball(ctx, *, phrase: str):
  num=random.randint(0, 6)
  Magic8ball=balllist[num]
  await ctx.reply("The magic 8 ball thinks "+Magic8ball+" about you"+phrase)
@bot.command()
async def joke(ctx):
  url="https://v2.jokeapi.dev/joke/Dark?format=json&blacklistFlags=nsfw,explicit,political,religious,sexist&type=twopart"
  
  req = requests.get(url)
  data = req.json()
  setup = data["setup"]
  punchline = data["punchline"]
  await ctx.send(setup)
  await asyncio.sleep(3)
  await ctx.send(punchline)

  
@bot.command()
async def weather(ctx, zip):
  my_secret = os.environ['Weather api']
  url="https://api.openweathermap.org/data/2.5/weather?zip="+zip+",US&appid="+my_secret
  req = requests.get(url)
  data=req.json
  weather = data["weather"][0]["description"]
  temp=data["main"]["temp"]
  temp=(temp - 273.15) * 9/5 + 32
  temp=temp.round(temp,1)
  await ctx.send(weather+" at "+str(temp)+"F")


@bot.command()
async def achRPS(ctx,*, phrase: str):
  RPSlist=["rock","paper","scissors"]
  bot=random.choice(RPSlist)
  phrase=phrase.lower()
  if bot=="rock" and phrase== 'rock':
    await ctx.reply("**It's a tie!**")
  if bot=="rock" and phrase== 'scissors':
    await ctx.reply("**You lose!**")
  if bot=="rock" and phrase== 'paper':
    await ctx.reply("**You win!**")
  if bot=="paper" and phrase== 'rock':
    await ctx.reply("**You lose!**")
  if bot=="paper" and phrase== 'paper':
    await ctx.reply("**It's a tie!**")
  if bot=="paper" and phrase== 'scissors':
    await ctx.reply("**You win!**")
  if bot=="scissors" and phrase== 'rock':
    await ctx.reply("**You win!**")
  if bot=="scissors" and phrase== 'paper':
    await ctx.reply("**It's a lose!**")
  if bot=="scissors" and phrase== 'scissors':
    await ctx.reply("**Its a tie!**")
#s
#p
#a
#c
#e
@bot.event
async def on_connect():
  print("your bot is online")
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