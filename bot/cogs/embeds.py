import discord
from discord.ext import commands
from datetime import datetime

client = discord.Client()


class embeds(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog has been successfully loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("embed commands - ✔️ ")

    # cog usage 
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def announcement(self, ctx, *, texts, amount=1):
        await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title="Announcement", description=texts, colour=0x00649b,  timestamp=ctx.message.created_at)
        emb.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        emb.set_thumbnail(url="Set thumbail url here")
        await ctx.channel.send(embed=emb)
      
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def embed(self, ctx, *, texts):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title=texts, colour=0x00649b)
        await ctx.channel.send(embed=emb)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def long_embed(self, ctx, title, *, texts):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title=title.replace("|", " "), colour=0x00649b, description=texts)
        await ctx.channel.send(embed=emb)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def image_embed(self, ctx, title, image, *, texts):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title=title, description = texts, colour=0x00649b)
        emb.set_image(url=image)
        await ctx.channel.send(embed = emb)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def imageonly(self, ctx, image):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(colour=0x00649b)
        emb.set_image(url=image)
        await ctx.channel.send(embed = emb)
		
		

def setup(client):
    client.add_cog(embeds(client))
