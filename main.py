# Main bot file for the ntoskrnl-bot framework. This file only handles the 
# "help" and "reload" commands, and loading of other commands. All other 
# commands can be found in the modules/ folder.

import discord
import asyncio
import time
import logging
import modules
import config
import traceback
import importlib
from datetime import datetime
from key import token

first_execution = time.monotonic()

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

class DiscordClient(discord.Client):
	def __init__(self):
		self.first_execution = 2147483647
		super().__init__()
		self.command_count = 0

	def run(self, *args, **kwargs):
		self.first_execution = time.monotonic()
		super().run(*args, **kwargs)


client = DiscordClient()

async def handleHelp(command: str, client, message):
	command = command.split(" ")

	if command[0] == "":
		basic_help = modules.get_basic_help()
		embed = discord.Embed(title=f"Help for {config.full_bot_name}", description=f"For detailed help about a command, run `{config.default_prefix} help <command>`.\nTo request a new command or feature, ping or message {config.owner}.", colour=0x06b206)
		for module, help_str in basic_help.items():
			if help_str is not None:
				embed.add_field(name=config.default_prefix+" "+module, value=help_str+"\n", inline=False)

	if command[0] != "":
		try:
			returned_help = modules.module[command[1]]
			returned_help = returned_help.detailed_help
		except KeyError:
			embed = discord.Embed(title=f"Help for command `{command[1]}`", description=f"Unknown command `{command[1]}`", colour=0xa20303)
		else:
			embed = discord.Embed(title=f"Help for command `{command[1]}`", colour=0x06b206)
			for internal_id, display_name in modules.detailed_help_fields:
				if returned_help[internal_id] is not None:
					embed = embed.add_field(name=display_name, value=returned_help[internal_id], inline=False)

	embed = embed.set_footer(text=str(datetime.now()))
	await message.channel.send(embed=embed)


@client.event
async def on_ready():
	modules.load(client)
	log.info(f"[{str(datetime.now())}] Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})")


@client.event
async def on_message(message):
	try:
		if (message.author.id == client.user.id) or message.author.bot:  # ignore message if from self or another bot
			return
		if message.channel.id not in config.log_channel_ignore:  # don't log messages from channels in the blacklist
			log.debug(f"[{str(datetime.now())}] [{message.guild.name}] [#{message.channel.name}] {message.author.name}#{message.author.discriminator}: {message.content}")

		if not any([message.content.startswith(prefix) for prefix in config.prefixes]):
			return  # ignore message if doesn't start with prefix

		parts = message.content.split(" ", 2)
		command = message.content.replace(parts[0]+" ", "")

		try:  # we'll see if the user provided a second command, if not print generic help
			if parts[1] == "help":
				client.command_count += 1
				await handleHelp(command=command, client=client, message=message)
				return
		except IndexError:
			client.command_count += 1
			await handleHelp(command="", client=client, message=message)
			return

		if command == "reload":
			client.command_count += 1
			importlib.reload(modules)
			modules.load(client)
			await message.add_reaction("☑")
			return

		try:
			client.command_count += 1
			await modules.module[parts[1]].handle(command=command, client=client, message=message)
		except KeyError:
			await message.channel.send(f"Sorry, that command wasn't found. (command: {parts[1]})")

	except Exception as e:
		if isinstance(e, UnicodeEncodeError):
			pass
		if isinstance(e, SystemExit):
			raise
		if isinstance(e, discord.errors.HTTPException):
			await message.channel.send(f"{message.author.mention} Sorry, but it looks like there was an error sending the response back to Discord. You probably issued a command that caused me to exceed my 2000 character message limit.")
			return
		stackdump = ''.join(traceback.format_exc())
		embed = discord.Embed(title="Internal error", description=f"Looks like there was an error, sorry. Please ping or message {config.owner} with this stackdump:\n```{stackdump}```", colour=0xf00000)
		embed = embed.set_footer(text="Error occurred at " + str(datetime.now()))
		await message.channel.send(embed=embed)
		log.exception(f"[{str(datetime.now())}] Error processing message: {message.content}")
		pass

client.run(token)
