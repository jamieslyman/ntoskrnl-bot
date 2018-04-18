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


basic_help = None
detailed_help = {
	"usage": f"`{config.default_prefix} time`",
	"args": None,
	"desc": "Prints the current UTC time, in a neat format.",
	"ex": f"`{config.default_prefix} time`",
	"perms": "Send Messages",
	"related": None,
}


def load(client):
	log.debug(f"[{str(datetime.now())}] successfully loaded module time")
	return


async def handle(command: str, client, message):
	embed = discord.Embed(title="Current UTC Time", description=f"{str(datetime.now())}\n{time.ctime()}", colour=0x06b206)
	await message.channel.send(embed=embed)
