import discord
from discord.ext import commands
from datetime import datetime
from data import *

client = discord.Client()


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog has been successfully loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("help commands - ✔️ ")

    # cog usage
    @commands.command()
    async def help(self, ctx):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Help", colour=0x00649b)
        for command in help_:
            emb.add_field(name=command[0], value=command[1])
        emb.set_thumbnail(url="Set thumbnail url here")
        await ctx.channel.send(embed=emb)
      
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def adminhelp(self, ctx):
        emb = discord.Embed(title="Admin-Help", colour=0x00649b)
        for command in adminhelp:
            emb.add_field(name=command[0], value=command[1])
        emb.set_thumbnail(url="Set url thumbnail here")
        emb.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=emb)
		
		

def setup(client):
    client.add_cog(help(client))
