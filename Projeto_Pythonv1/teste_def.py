from time import sleep
import discord
import os
import pytube as pt
import moviepy.editor as mp
from time import sleep
from pytube import YouTube

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
dados = {}
https = list()
playList = https[:]
aaa = 0
podebaixar = -1
@client.event
async def on_ready():
    print("O BOT ESTÁ ONLINE")


@client.event
async def on_message(message):
    global https
    global playList
    global aaa
    global podebaixar
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention
    con = 0
    # Previnir erro
    if author == "TangerBOT":
        return

    if content == "bom dia" and channel.name == "bom-dia":
        await channel.send("bom dia " + mention)
    if content == 'pkk':
        await channel.send(
            file=discord.File(f'Coldplay - Yellow (Official Video).mp4'))
    if content == "cima":
        await message.add_reaction("⬆")
    if content == 'url:':
        await channel.send('Digite a url:')
        if author not in dados:
            dados[author] = len(dados)
        podebaixar = dados[author]
        print('podebaixar=', podebaixar)
        await channel.send(author)
        await channel.send(dados)
        aaa += 1
        await channel.send(f'pronto, modo download abilitado para {author}:')
        await channel.send('Você pode enviar url a qualquer momento para baixar a música')
    else:
        print(aaa)
        if aaa == 0:
            await channel.send('Para baixar músicas digite "url:"')
    if 'https'[0:5] in content and con == 0:
        print(f"DADOS={dados[author]}")
        print(f"PODE={podebaixar}")
        https.append(str(f"'{message.content}'"))
        playList = https[:]
        print(f'ok con = {con} e Author {author}')
        con += 1
        print(f'https = {https}')
        if dados[author] == podebaixar:
            await channel.send('Estou enviando, um momento')
            url = https[0]
            print(f'URL = {url}')
            yt = YouTube(url)
            yt.streams.first().download()
            tiltle = yt.streams.first().download()[50:]
            sleep(2)
            await channel.send(file=discord.File(f'{tiltle}'))
            https.clear()
        else:
            await channel.send('Ops, parece que ocorreu um erro, tente digitar "url:" novamente, por favor')
# print(f'pode baixar {dados[author]}')
            # print(f'{dados[author]} = {podebaixar}')
            # print(f'{dados[author]} = {podebaixar}')
            # print('Iniciando download')
            # print('-------→', playList)
            # url = https[0]
            # print('-------→', url)
            # stream = pt.YouTube(url=url).streams.get_audio_only()
            # stream.download('mp4')
            # title = str(stream.title)
            #
            # # conversão
            # clip = mp.AudioFileClip(f'mp4\\{title}.mp4')
            # clip.write_audiofile(f'mp3\\{title}.mp3')
            # print('Aguarde')
            # print('prontinho')
            # print(f'mp3/{title}.mp3')
# # Deletar mp4
#
# delete = str(input('Deletar mp4? (S/N): '))
# if delete in 'Ss':
#     os.remove('mp4\\' + title + '.mp4')
#     print('.mp4 deletado!')
# else:
#     print('.mp4 não deletado!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(791756036322361354)
    await channel.send("bom dia" + member.mention)


client.run("ODcyMjQyMTI2ODExOTg3OTc4.YQnAyA.UVYiwBgCF9NdUG9TIKv7jz1K2sk")
