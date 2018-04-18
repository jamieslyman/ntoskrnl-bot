# ntoskrnl-bot
A simple, fast, and modular Discord bot written in Python

## Requirements
 - Python 3.6+
 - discord.py **rewrite branch**
 - that's actually about it, really

## Setup
Once you've cloned the code, you'll need to change a few things. Open up `config.py` and change these things:
 - set `main_loglevel`, `file_loglevel`, and `term_loglevel` to appropriate values. Values are shown in the comment on line 4
 - set `logfile` to the file you'd like to log to
   - at the time being, it is not possible to completely disable logging, however it might work if you set the logfile to `/dev/null` (no guarantees on that working though)
   - disabling logging is a planned feature
 - channels that you'd like content not to be logged for (such as administrator channels) can be ignored by adding their channel ID to `log_channel_ignore`
 - next, enter the bot's full name under `full_bot_name`
 - then, in `invite_url`, replace `{your bot id}` with your bot's user id
 - set your username and discriminator in the `owner` variable, the bot will refer to this person as the owner of the bot (or rehost)
 - you can set the prefix the bot uses in `default_prefix`, and set all prefixes it will respond to in `prefixes`
   - it is necessary to have whatever you set `default_prefix` to be to be in `prefixes` as well
   - it is __very__ highly recommended that mentioning the bot will trigger it as well, so replace {your bot id} with the bot's user id number

Finally, open up `key.py` and set `token` to the token of your bot's user account.

## Adding Commands/Modules
Whenever a command is run in the bot, if it's not a `help` or `reload` command, the bot will look for a module with that command's name. `modules/__template__.py` is a template that you can use to write new commands. Here is how you write or add a new command to the bot:
 - head into `modules/` and make a copy of `__template__.py`
 - set the `basic_help` variable and the fields in the `detailed_help` dictionary
 - write your `load()` function. this function will be synchronously run whenever the module is loaded.
   - **NOTE: This function very well might run multiple times, if the bot loses and regains internet connectivity. Make sure your function can handle this.**
   - **NOTE: This function is run synchronously, and so async code cannot be run.** (It is planned to later move the code to support async, however by early judgment, this would require a bit more effort.)
 - write your `handle()` function. This function will be called if the bot knows for sure your command has been run, so it is not necessary to recheck that. If you really wish, the original message object is passed as a parameter if you desire to do so.
   - This function is run asynchronously, unlike the `load()` function.
 - Once you have all your code written, save it as {command}.py. If the name conflicts with a module in the standard library (eg. `time`), save it as some other name. What specifically does not matter since the problem will be rectified in the next step:
 - Open up the `__init__.py` file. Import your new file at the top, in between the two comments that tell you where to import them. (If you want to get technical, where you put the import statement does not matter but I highly recommend you import it in the space given, for clarity.)
 - Under the `module` dictionary, create a new dictionary entry where the key is the string that you want to trigger the command with, and the value should be set to the module object you imported.

## Known Problems/Drawbacks
 - The bot **will not work** with a character-based prefix, such as `!` or `%%`. A short word must be used instead, such as `ntbot`.
   - If a character prefix is used, it will still technically work but a space must be put after it; for example `!help` would be `! help`.
   - This is planned to be fixed at some point.
 - An empty string (or string with only whitespace) cannot be used as a value in either `basic_help` or `detailed_help`.
   - This is a discord.py limitation.

## Credits
Massive thanks to Rapptz and contributors for their work on the discord.py library.  
Thanks to DrHypercube for coming up with the original idea to modularize the code.  
