import json
import discord
from discord.ext import commands

with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']

activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

intents = discord.Intents.default()
intents.members = True
#  client = discord.Client(intents=intents)
channel = client.get_channel(875828784450904114)
await channel.send('hello')

