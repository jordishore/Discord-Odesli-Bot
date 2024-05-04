import os
import sys
import re
import logging
import requests
import discord
from discord import app_commands
from dotenv import load_dotenv
import requests.utils

logger = logging.getLogger('discord-odesli-bot')
logger.setLevel(logging.INFO)
logger.handler = logging.StreamHandler(sys.stdout)
logger.handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger.handler.setFormatter(formatter)
logger.addHandler(logger.handler)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class OdesliBot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

class SongLink():
    def __init__(self):
        self.api_base = 'https://api.song.link/v1-alpha.1/links?url='
        self.country_code = 'AU'
    async def get_link(self, url):
        link = self.api_base + url + self.country_code
        url_encoded = requests.utils.requote_uri(link)
        logger.info(f'Getting Songlink')
        request = requests.get(url_encoded, timeout=300)
        data = request.json()
        logger.info(data)
        songlink = str(data['pageUrl'])
        logger.info(f'Songlink: {songlink}')
        return songlink


intents = discord.Intents.default()
client = OdesliBot(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command(name='songlink', description='Shares a universal link to the channel')
@app_commands.rename(user_link='url')
@app_commands.describe(user_link='Enter the sahre URL from your streaming platform. This will be converted to a universal link.')
async def get_link_slash_command(interaction: discord.Interaction, user_link: str):
    response = await SongLink().get_link(url=user_link)
    typere = re.search(r"\/\/([\w]*)\.", response)
    type = typere.group(1)
    if type == "album":
        grammar = "an"
    else: grammar = "a"
    await interaction.response.send_message(f'{interaction.user.mention} shared {grammar} {type}.\n{response}')


@client.tree.context_menu(name='Get Universal Link')
async def get_link_from_message(interaction: discord.Interaction, message: discord.Message):
    print(message.content)
    response = await SongLink().get_link(url=message.content)
    await interaction.response.send_message(f'{response} {interaction.user.mention}', ephemeral=True)


client.run(token)
