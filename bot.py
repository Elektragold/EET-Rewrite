import lightbulb
import hikari
import keep_alive

import os

bot = lightbulb.BotApp(
    token=os.environ['BOT_TOKEN'],
    prefix='$',
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(848155636549156864)
)
bot.load_extensions_from("./extensions")

keep_alive.keep_alive()
bot.run()
