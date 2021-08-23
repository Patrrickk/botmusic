from discord.ext import commands
import discord
import io
import aiohttp

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channel = client.get_channel(823529603121021012)
    if message.author == client.user:
        return

    if message.content == 'ze':
        await message.channel.send(file=discord.File('imagens/uhul.gif'))

    if message.content == 'mu':
        def my_after(error):
            coro = error.some_channel.send('Song is done!')
            fut = error.asyncio.run_coroutine_threadsafe(coro, client.loop)
            try:
                fut.result()
            except:
                pass
        channel.voice.play(
            discord.FFmpegPCMAudio("https://youtu.be/UjnDpcgJXvA?list=PLAsTje28QYlz9gNCc0LCvKQH46CpUddMB"),
            after=my_after)


client.run("ODcyMjQyMTI2ODExOTg3OTc4.YQnAyA.UVYiwBgCF9NdUG9TIKv7jz1K2sk")
