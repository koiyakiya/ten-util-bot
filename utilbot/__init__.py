import dotenv
import os

# Load the enviornment variables.
dotenv.load_dotenv()

"""
Change to `False` to disable debug mode and use the production database.
"""
debug_mode = True

"""
Change to `True` to wipe the debug database on bot exit.
Will only work if `debug_mode` is set to `True`.
"""
wipe = True

# Constant paths for use throughout the bot
__DEBUG_DB_PATH__ = "db/debug.db"
__PROD_DB_PATH__ = "db/prod.db"
__EXTENSIONS_PATH__ = "utilbot/extensions"

# Discord bot token (Always change in .env)
__TOKEN__ = os.environ["TOKEN"]

