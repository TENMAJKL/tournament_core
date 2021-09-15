import discord
from discord.ext import commands
from datetime import datetime
from data import *
import requests
import os
from PIL import Image, ImageDraw, ImageFont

client = discord.Client()


class utils(commands.Cog):

	def __init__(self, client):
		self.client = client

	# cog has been successfully loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print("Data commands - ✔️ ")

	# cog usage
	@commands.command()
	async def player(self, ctx, *, name):
		token = os.getenv("core_token")
		data = requests.get(f"https://slh.tenmajkl.repl.co/data/api/{token}/{name}").json()
		""" 

        This was supposed to be system to generate images with the data, it was pain and never done.

        data = {"data":{"Assists":"10.0","DPR":"0.556","Deaths":"10.0","KD":"1.0","KPR":"0.556","Kills":"10.0","SLR":"1.185","SVR":"1.527","Team":"frajeri","device":"asdadsasd","id":"123456789"},"name":"ads","responce":"sucess"}

		if data.get("responce") != "not found":
			data = data.get("data")

			img = Image.open("./static/bot_design.png")
			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("./static/ufonts.com_bank-gothic-medium.ttf", 40)
			draw.text((480, 58), name, font=font)
			draw.text((450, 113), data.get("Team"), font=font)
			draw.text((374, 165), data.get("id"), font=font)
			draw.text((450, 214), data.get("device"), font=font)
			
			img.save("./static/parek.png")
        """
        # Cheap i know
        await ctx.channel.send(data)

	@commands.command()
	async def team(self, ctx, *, name):
		token = os.getenv("core_token")
		data = requests.get(f"https://slh.tenmajkl.repl.co/clans/api/{token}/{name}").json()

		
		if data.get("responce") != "not found":
			stats = data.get("data")
			emb = discord.Embed(title="Clan Statistics", description=f"Statistics of {name}", color=0x00649b)

			for stat in stats.keys():
				emb.add_field(name=stat, value=stats.get(stat), inline=True)
			
			players = data.get("players")

			players_list = ""

			for player in players:
				players_list += player.get("name") + "\n"
			
			emb.add_field(name="Players", value=players_list)

		else:
			emb = discord.Embed(title="Clan Statistics", description="Not found", color=0x00649b)
		
		await ctx.channel.send(embed = emb)
			

def setup(client):
    client.add_cog(utils(client))
