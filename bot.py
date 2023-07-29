import logging
import os
import sys
import time

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger('discord-odesli-bot')
logger.setLevel(logging.INFO)
logger.handler = logging.StreamHandler(sys.stdout)
logger.handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger.handler.setFormatter(formatter)
logger.addHandler(logger.handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


def get_link(url):
    api_link = "https://api.song.link/v1-alpha.1/links?url=" + url + "&userCountry=AU" #update country code to suit
    logger.info(f'Getting Songlink')
    request = requests.get(api_link)
    data = request.json()
    songlink = str(data['pageUrl'])
    logger.info(f'Songlink: {songlink}')
    return songlink


@bot.event
async def on_ready():
    logger.info(f'{bot.user.name} has connected to Discord!')


@bot.command(name='sl')
async def sl(ctx, songlink: str):
    logger.info(f'{ctx.author.display_name} shared: {ctx.message.content}')
    response = get_link(songlink)
    await ctx.send(f"{ctx.author.mention} shared a song: {response}")
    logger.info('Deleting original message...')
    await discord.Message.delete(ctx.message, delay=10)

@bot.event
async def on_message_delete(message):
    logger.info(f'Message {message.id} has been deleted.')
    


bot.run(TOKEN)
