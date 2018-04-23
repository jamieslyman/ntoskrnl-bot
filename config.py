# Configuration options

# log settings, required for use
main_loglevel = 10  # Debug: 10, Info: 20, Warn: 30, Err: 40, Crit: 50
file_loglevel = 20
term_loglevel = 10
logfile = "bot.log"
logformat = "%(message)s"
log_channel_ignore = [  # list of channel IDs to not log messages from (eg. an administrator channel)
]

# meta information about the bot
full_bot_name = "your bot name"
bot_version = "ntoskrnl-bot framework 0.8.1"
invite_url = "https://discordapp.com/api/oauth2/authorize?client_id={your bot id}&permissions=506850386&scope=bot"


owner = "@your username and discriminator"  # this line should be set to whoever operates the bot (or rehost)

# prefixes the bot uses
default_prefix = "ntbot"
prefixes = [
	"ntbot",
	"<@{your bot id}>",
]
