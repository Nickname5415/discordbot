import discord
import random
import requests
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def goodbye(ctx):
    await ctx.send(f'Adios, {bot.user}!')

@bot.command()
async def mem(ctx):
    XD = random.randint(1,4)
    if XD == 1:
        with open('images/mem1.jpg', 'rb') as f:
         
            picture = discord.File(f)
        
        await ctx.send(file=picture)
    elif XD == 2:
        with open('images/mem2.jpg', 'rb') as f:
         
            picture = discord.File(f)
        
        await ctx.send(file=picture)
    elif XD == 3:
        with open('images/mem3.jpg', 'rb') as f:
         
            picture = discord.File(f)
        
        await ctx.send(file=picture)
    
    elif XD == 4:
        with open('images/mem4.jpg', 'rb') as f:
         
            picture = discord.File(f)
        
        await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox,
    el programa llama a la función get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("MTIxNjkyMjgyNTU3OTk1NDIzNw.Gpub3-.lsNYitvk-q-hgnjYWjhAx7mz-sRI3hcfidj5ng")