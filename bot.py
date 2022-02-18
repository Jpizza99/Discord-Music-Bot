from musicbot import music_cog
import discord
from discord.ext import commands


Bot = commands.Bot(command_prefix='/')

Bot.add_cog(music_cog(Bot))

token = ''
with open('token.txt', 'r') as tok:
    token = tok.read()

Bot.run(token)