import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


def get_link(url):
    api_link = "https://api.song.link/v1-alpha.1/links?url=" + url + "&userCountry=AU" #update country code to suit
    request = requests.get(api_link)
    data = request.json()
    songlink = str(data['pageUrl'])
    print(songlink)
    return songlink


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='sl')
async def sl(ctx, songlink: str):
    response = get_link(songlink)
    await ctx.send(response)


bot.run(TOKEN)
