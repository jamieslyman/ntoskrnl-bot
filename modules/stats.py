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

basic_help = f"shows various running statistics of {config.full_bot_name}"
detailed_help = {
	"usage": f"`{config.default_prefix} stats`",
	"args": None,
	"desc": f"This command shows different available statistics of {config.full_bot_name}, including servers, uptime, and commands run.",
	"ex": f"`{config.default_prefix} stats`",
	"perms": "Send Messages",
	"related": f"`{config.default_prefix} info` - shows information about {config.full_bot_name}}",
}


def load(client):
	log.debug(f"[{str(datetime.now())}] successfully loaded module {__name__}")
	return


async def handle(command: str, client, message):
	embed = discord.Embed(title=f"{config.full_bot_name} stats", description=discord.Embed.Empty, color=0x404040)
	embed = embed.add_field(name="Uptime", value=f"{str(int(time.monotonic()-client.first_execution))} seconds")
	embed = embed.add_field(name="Servers", value=len(client.servers))
	embed = embed.add_field(name="Total commands run since last reboot", value=client.command_count)
	embed = embed.set_footer(text=time.ctime())
	await client.send_message(message.channel, embed=embed)
