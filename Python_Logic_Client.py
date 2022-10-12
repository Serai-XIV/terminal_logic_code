from distutils.cmd import Command
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=";")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a robot")

bot.run("MTAyNDEyNjk1NTU0Njc0NjkyMg.GT8Hlp.D92ReYMR8LI8pXaNOuLRDrVC6GrZ3TZLrwto5c")
