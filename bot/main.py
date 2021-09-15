import discord
import json
import os
import dotenv
import requests
#If repl from keep_alive import keep_alive
from data import roles

from discord.ext import commands
from dotenv import load_dotenv




intents = discord.Intents().default()
intents.members = True
intents.presences = True
intents.reactions = True
client = commands.Bot(command_prefix = "sln/", intents=intents)
client.remove_command("help")
load_dotenv()
TOKEN = os.getenv('TOKEN')



@client.event  
async def on_ready():
	print("-------------------------")
	print("Bot Name: " + client.user.name)
	print(client.user.id)
	print("API Version: " + discord.__version__)
	print(client.latency * 1000)
	print("-------------------------")

	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="StarLight Network"))



@client.event
async def on_raw_reaction_add(payload):
	if payload.channel_id == 803463159759241221:
		if payload.emoji.name in roles:
			guild = client.get_guild(payload.guild_id)
			role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
			await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
	if payload.channel_id == 803463159759241221:
		if payload.emoji.name in roles:
			guild = client.get_guild(payload.guild_id)
			role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
			await guild.get_member(payload.user_id).remove_roles(role)


for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#keep_alive()
client.run(TOKEN)
