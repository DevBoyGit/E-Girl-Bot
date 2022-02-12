# bot.py
import asyncio
import os

import discord
from discord.ext import commands as cmd
from dotenv import load_dotenv
import random
import youtube_dl

bot = cmd.Bot(command_prefix='!')

client = discord.Client()

allowed_roles = ["MODERATOR", "OWNER"]

@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    if ctx.message.author.top_role.name not in allowed_roles:
        await ctx.reply("You do not have the permission to use this command!")
        return

    reason_message = reason
    if member == None or member == ctx.message.author:
        await ctx.channel.send("> You cannot kick yourself!")
        return
    if reason_message == None:
        reason_message = "> Breaking the rules"
    else:
        reason_message = reason_message.replace("_", " ")
        reason_message = reason_message.capitalize()

    message = f"**You have been banned from {ctx.guild.name} for \"{reason_message}\"**\nThis message was sent automatically"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"> {member} is banned!")


@bot.command()
async def kick(ctx, member:discord.Member, reason):
    if ctx.message.author.top_role.name not in allowed_roles:
        await ctx.reply("You do not have the permission to use this command!")
        return

    reason_message = reason
    if member == None or member == ctx.message.author:
        await ctx.channel.send("> You cannot kick yourself!")
        return
    if reason_message == None:
        reason_message = "> Breaking the rules"
    else:
        reason_message = reason_message.replace("_", " ")
        reason_message = reason_message.capitalize()

    message = f"**You have been kicked from {ctx.guild.name} for \"{reason_message}\"**\nThis message was sent automatically"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason_message)
    await ctx.channel.send(f"> {member} is kicked!")


@bot.command()
async def simp(ctx):
    await ctx.reply("> Bruh down bad lol")

@bot.command(name="funfact")
async def fun_fact(ctx):
    fact = get_random_fact()
    await ctx.reply(content=f"> **Fun fact:** {fact}")

def get_random_fact(file="facts.txt"):
    fact = ""
    with open(file, "r") as facts:
        rand = random.Random()

        for i in range(0, rand.randint(0, 3090)):
            fact = facts.readline()

    return fact



# youtube_dl.utils.bug_reports_message = lambda: ''
#
# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
# }
#
# ffmpeg_options = {
#     'options': '-vn'
# }
#
# ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
#
#
# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=0.5):
#         super().__init__(source, volume)
#         self.data = data
#         self.title = data.get('title')
#         self.url = ""
#
#     @classmethod
#     async def from_url(cls, url, *, loop=None, stream=False):
#         loop = loop or asyncio.get_event_loop()
#         data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
#         if 'entries' in data:
#             # take first item from a playlist
#             data = data['entries'][0]
#         filename = data['title'] if stream else ytdl.prepare_filename(data)
#         return filename
#
#
# @bot.command()
# async def join(ctx):
#     if not ctx.message.author.voice:
#         await ctx.reply(f"> {ctx.message.author.name} is not connected to a voice channel")
#         return
#     else:
#         channel = ctx.message.author.voice.channel
#     await channel.connect()
#
#
# @bot.command()
# async def leave(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_connected():
#         await voice_client.disconnect()
#     else:
#         await ctx.send("> The bot is not connected to a voice channel.")
#
#
# @bot.command()
# async def play(ctx, url):
#     try:
#         server = ctx.message.guild
#         voice_channel = server.voice_client
#
#         async with ctx.typing():
#             filename = await YTDLSource.from_url(url, loop=bot.loop)
#             voice_channel.play(discord.FFmpegPCMAudio(executable="EGirlBot\\ffmpeg.exe", source=filename))
#         await ctx.send(f'> Now playing: {filename}*')
#     except():
#         await ctx.send("> ERROR: The bot is not connected to a voice channel.")
#
#
# @bot.command()
# async def pause(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_playing():
#         await voice_client.pause()
#     else:
#         await ctx.send("> The bot is not playing anything at the moment.")
#
#
# @bot.command()
# async def resume(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_paused():
#         await voice_client.resume()
#     else:
#         await ctx.send("> The bot was not playing anything before this. Use play_song command")
#
#
# @bot.command()
# async def stop(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_playing():
#         await voice_client.stop()
#     else:
#         await ctx.send("The bot is not playing anything at the moment.")
#
#

load_dotenv()

bot.run(os.getenv("TOKEN"))
