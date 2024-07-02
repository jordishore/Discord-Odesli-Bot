# Discord bot for Odesli (formerly Songlink)

Everyone can now enjoy the music you share no matter what platform they use.

This is a simple bot that takes a share URL from your streaming platform and returns a universal link so that everyone can easily enjoy the music you share.

## Getting Started

### Discord Prep

 1. Create Application via [Discord Developer Portal](https://discord.com/developers/) - give it a fun name
 2. Configure your bot via the 'Bot' tab - ensure you have enabled 'message content intent'
 3. Generate and take note of your bot token you will need this when creating your .env file below
 4. Copy your application ID from the general information tab
 5. Add bot to your server using the following link, inserting your application ID after `id=`: `https://discord.com/api/oauth2/authorize?client_id=&permissions=137439217728&scope=bot`

### Python Prep

 1. Download the source code zip from the releases tab
 2. Install from the requirements.txt [How-To](https://note.nkmk.me/en/python-pip-install-requirements/)
 3. Create a .env file in the package directory and include the following lines: `DISCORD_TOKEN=<YOUR-BOT-TOKEN>`

## Usage

- Slash Coomand: Enter the URL from your streaming platform and the bot will return a universal link.
- From Message: Right Click on a message with a URL from your streaming platform and select 'Get Universal link'. The bot will message the channel with the universal link, this message is ephemeral.

![Example Usage](https://github.com/jordishore/Discord-Odesli-Bot/blob/v2/examples/v2-example_usage_video.gif?raw=true)

### Supported Streaming Platforms

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

## Credits

- Powered By [Odesli](https://odesli.co/)

## Disclaimer

This bot was built as a personal project and is in no way affiliated with Odesli/SongLink. For Odesli's terms of service and API information please refer to <https://odesli.co/>
