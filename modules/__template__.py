import discord
import asyncio
import logging		# these are the basic imports you're likely to need
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

# basic_help is a one-line explanation of what the command does. to omit the command from generic help, set it to None.
# note however this *cannot* be an empty string or one with only whitespace
basic_help = None
detailed_help = {  # detailed help, shown when running `{prefix} help command`. any field can be set to None to be omitted
	# the same rule about strings applies to each field here as well.
	"usage": None,  # set this to a string, like "`{prefix} example <argument> [optional]`"
	"args": None,  # description of arguments in the command
	"desc": None,  # detailed description of what the command does
	"ex": None,  # example use of the command, like "`{prefix} example 42 cheese`" or "`{prefix} example anchovies`"
	"perms": None,  # permissions required to run the command properly
	"related": None,  # other commands that might be related to this command
}


def load(client):
	# first time setup. this function is passed the newly setup client as the only argument.
	# good for setting up a background processing loop for eg. music playback.
	log.debug(f"[{str(datetime.now())}] successfully loaded module {__name__}")
	return


async def handle(command: str, client, message):
	# do some stuff in response to the command being run - say hi, update a role, etc.
	return