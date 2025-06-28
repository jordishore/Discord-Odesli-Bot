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
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

logger.file_handler = logging.FileHandler(filename='discord-odesli-bot.log', encoding='utf-8', mode='w')
logger.file_handler.setLevel(logging.DEBUG)
logger.file_handler.setFormatter(formatter)

logger.console_handler = logging.StreamHandler(sys.stdout)
logger.console_handler.setLevel(logging.INFO)
logger.console_handler.setFormatter(formatter)

logger.addHandler(logger.file_handler)
logger.addHandler(logger.console_handler)

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
        self.country_code = '&userCountry=AU'

    async def get_link(self, url):
        link = self.api_base + url + self.country_code
        url_encoded = requests.utils.requote_uri(link)
        logger.info('Getting Songlink')
        logger.info(f'request URL: {url_encoded}')
        request = requests.get(url_encoded)
        data = request.json()
        logger.debug(f'response: \n {data}')
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
@app_commands.describe(
    user_link='Enter the share URL from your streaming platform. '
    'This will be converted to a universal link.'
)
async def get_link_slash_command(interaction: discord.Interaction, user_link: str):
    url_encoded_user_link = requests.utils.requote_uri(user_link)
    response = await SongLink().get_link(url=url_encoded_user_link)
    typere = re.search(r"\/\/([\w]*)\.", response)
    type = typere.group(1)
    if type == "album":
        grammar = "an"
    else:
        grammar = "a"
    await interaction.response.send_message(f'{interaction.user.mention} shared {grammar} {type}.\n{response}')


# context menu command
@client.tree.context_menu(name='TESTING - Get Universal Link')
async def get_link_from_message(interaction: discord.Interaction, message: discord.Message):
    # FIXES - https://github.com/jordishore/Discord-Odesli-Bot/issues/8
    # defer the response to avoid timeout, puts bot into thinking state
    await interaction.response.defer(ephemeral=True)
    url_from_message = re.search("(?P<url>https?://[^\\s]+)", message.content).group("url")
    logger.info(f'input URL: {url_from_message}')
    response = await SongLink().get_link(url=url_from_message)
    # send the response
    await interaction.followup.send(f'{response} {interaction.user.mention}', ephemeral=True)

client.run(token)
