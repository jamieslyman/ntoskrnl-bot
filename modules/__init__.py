import sys; sys.path.append("modules/")

# to import new commands, add them to the list below. note that
# PyCharm will throw errors for the names but the above line fixes that

# import example
import cmd_time
import stats
import info

# to import new commands, add them to the list above

import asyncio
import logging
import config
from datetime import datetime

# this dictionary is a lookup table of commands to modules. it exists to
# allow command aliases and to avoid name conflicts with eg. "time" module
# note/todo: adding aliases will make them show up twice in generic help
module = {
	"time": cmd_time,
	"stats": stats,
	"info": info,
	# add values to this dictionary to add commands.
	# if it's not in this table the command will not be recognized!
}

# the rest of this file should not need to be touched when simply adding commands

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

# list of fields in detailed help
detailed_help_fields = [
	# format:	("internal_id", "display_name")
	("usage", "Usage"),
	("args", "Arguments"),
	("desc", "Description"),
	("ex", "Examples"),
	("perms", "Required Permissions"),
	("related", "Related Commands"),
]


def get_basic_help():
	command_help = {}
	for key, val in module.items():
		command_help[key] = val.basic_help
	return command_help


# loads each new module. possible todo: run async?
def load(client):
	log.debug(f"[{str(datetime.now())}] modules.__init__: loading modules...")
	for m in module.values():
		m.load(client)
	log.debug(f"[{str(datetime.now())}] modules.__init__: done loading modules")
