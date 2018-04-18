import discord
import asyncio
import logging
import time
import config
from datetime import datetime

log = logging.getLogger(__name__)
log.setLevel(config.main_loglevel)
_log_format = logging.Formatter(config.logformat)
_log_fh = logging.FileHandler(config.logfile)
_log_fh.setFormatter(_log_format)
_log_sh = logging.StreamHandler()
_log_fh.setLevel(config.file_loglevel)
_log_sh.setLevel(config.term_loglevel)
log.addHandler(_log_sh)
log.addHandler(_log_fh)


basic_help = f"returns information about {config.full_bot_name}, including an invite url"
detailed_help = {
	"usage": f"`{config.default_prefix} info`",
	"args": None,
	"desc": "Shows information about the bot.\n",
	"ex": f"`{config.default_prefix} info`",
	"perms": "Send Messages",
	"related": f"`{config.default_prefix} stats` - shows running statistics about {config.full_bot_name}",
}


def load(client):
	log.debug(f"[{str(datetime.now())}] successfully loaded module {__name__}")
	return


async def handle(command: str, client, message):
	embed = discord.Embed(title=f"{config.full_bot_name} info", description=discord.Embed.Empty, color=0x404040)
	embed = embed.add_field(name="Version", value=config.bot_version)
	embed = embed.add_field(name="Invite Link", value=config.invite_url)
	embed = embed.set_footer(text=time.ctime())
	await message.channel.send(embed=embed)
	return
