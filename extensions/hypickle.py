import os
from aiohttp import request
import requests
import hikari
import lightbulb

hypickle_plugin = lightbulb.Plugin(name="hypickle", description="All commands related to hypixel")

@hypickle_plugin.command
@lightbulb.command(name="online", description="Checks whether the account is currently being used")
@lightbulb.implements(lightbulb.commands.SlashCommand)
async def check_online(ctx: lightbulb.context.Context) -> None:
    
    uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/Diablo_TDL").json()['id']
    params = {
		"key": os.environ["API_KEY"],
		"uuid": uuid
	}
    URL = "https://api.hypixel.net/status"
    
    async with request('GET', URL, params=params) as response:
        data = await response.json()
        if not data['success']:
            print(f"Hypixel:{data['cause']}")
            await ctx.respond(
                embed=hikari.Embed(
                    title='Status',
                    description="An error has occurred"
                ))
        else:
            embed = (
                hikari.Embed(
                    title='Status', 
                    description='Online' if data["session"]["online"] else 'Offline', 
                    color=0xFF5733
                    )
            )
        
            await ctx.respond(embed=embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(hypickle_plugin)

def unload(bot):
    bot.remove_plugin(hypickle_plugin)