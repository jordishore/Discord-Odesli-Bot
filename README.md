# Discord bot for Odesli (formerly Songlink)
A very simple bot that returns a song.link URL for songs shared to a channel using most major streaming platform's share URL's.


## Getting Started

### Discord Prep:
 1. Create Application via [Discord Developer Portal](https://discord.com/developers/) - give it a fun name
 2. Configure your bot via the 'Bot' tab - ensure you have enabled 'message content intent'
 3. Generate and take note of your bot token you will need this when creating your .env file below
 4. Copy your application ID from the general information tab
 5. Add bot to your server using the following link, inserting your application ID after `ID=`: `https://discord.com/api/oauth2/authorize?client_id=&permissions=137439217728&scope=bot`

### Python Prep:
 1. Download the source code zip from the releases tab
 2. Install from the requirements.txt [How-To](https://note.nkmk.me/en/python-pip-install-requirements/)
 3. Create a .env file in the package directory and include the following line: `DISCORD_TOKEN=<YOUR-BOT-TOKEN>`

## Usage
 1. Start the bot by running `bot.py` in your terminal
 2. Invoke the bot using `/sl` followed by the url of the song you wish to share. Please see below for a full list of support streaming platforms
 3. The bot will then reply with a song.link url for your song.
### Example:
- User sends: /sl https://tidal.com/browse/track/87166293
- Bot Replies: https://song.link/t/87166293
- Please see the 'Examples' folder for screenshots

### Supported Streaming Platforms:
- spotify
- itunes
- appleMusic
- youtube
- youtubeMusic
- google
- googleStore
- pandora
- deezer
- tidal
- amazonStore
- amazonMusic
- soundcloud
- napster
- yandex
- spinrilla
- audius
- anghami
- boomplay
- audiomack

## Credits & Inspiration
- [SongLink_Discord_Bot](https://github.com/EdgarLefevre/SongLink_Discord_Bot)
- [Odesli](https://odesli.co/)
## Disclaimer
This bot was built as a personal project and is in no way affiliated with Odesli/SongLink. For Odesli's terms of service and API information please refer to https://odesli.co/
