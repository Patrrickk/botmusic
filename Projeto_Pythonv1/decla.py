import csv

from discord.ext import commands
import discord
import io
import aiohttp
from pytube import YouTube, Playlist
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# guardar todos dados dos úsuarios
dados = list()

# salva temporariamente os dados de um usuário
pessoas = dict()

# salva temporariamente os nomes das músicas de um úsuario
nome_music = list()

# listas
list_musicas = list()
list_temp = list_musicas[:]
arquivos_baixados = []
# dicionários
usuarios = {}
links = {}
https = {}

quant_pessoas = 0

# paginas
pag = ''

# variáveis para mostra uma determinada quantidade músicas por vez
ini = 1
fim = 3
# Quem pode utilizar o bot
testadores = {'Pk': 698924189431759040, 'andrebr12': 698925348473274408, 'StitchN$': 827334161148149820}  # pk, andre
verificar = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # listas
    global dados, nome_music, gg
    # dicionários
    global usuarios, pessoas
    global quant_pessoas
    # variaveis simples
    global ini, fim, testadores, verificar, pag
    if message.author == client.user:
        return
    print(f'Tamanho 2 == {pag}')
    if message.author.name in testadores or len(pag) == 3:
        if message.author == client.get_user(testadores[message.author.name]):
            print(f'Tamanho == {pag}')
            # lista de músicas baixadas pelos users
            if message.content == 'lista' or len(pag) == 3:
                letras = ''
                if pag == '1️⃣':
                    ini = 1
                    fim = 3
                if pag == '2️⃣':
                    ini = 3
                    fim = 6
                if pag == '3️⃣':
                    ini = 6
                    fim = 8
                print(dados, 'SDJOASHDOAJSDAJÇSDJÇASJDÇAJSÇDJÇASJDÇAjsçd')
                for c in dados:
                    for pos, a in enumerate(c[message.author.name][ini:fim]):
                        letras += f'{pos + 1}º = {a}\n'
                    pag = ''
                    if message.author.name in c:
                        print(f'{c[message.author.name]} <><><><><><><><><><><><>')
                        await message.channel.send(message.author.mention)
                        gg = await message.channel.send(f'{letras}')
                        if len(c[message.author.name]) < 999:
                            await gg.add_reaction('1️⃣')
                        elif len(c[message.author.name]) > 2:
                            await gg.add_reaction('2️⃣')
                        elif len(c[message.author.name]) > 5:
                            await gg.add_reaction('3️⃣')
                    else:
                        await message.channel.send('Você ainda não baixou músicas')
                if len(dados) == 0:
                    await message.channel.send('Para acessar a lista, você precisa baixar uma música primeiro!')
            tube = ['https://www.youtube.com/watch?', 'https://youtu.be/']
            for li in tube:
                if li in message.content:
                    # pega a messagem (url) do author e colocar entre aspas
                    url = str(f'"{message.content}"')
                    # url do YouTube vídeo/audio padrão
                    yt = YouTube(url)
                    # extraindo só o audio
                    audio = yt.streams.filter(only_audio=True).first()
                    # baixando o arquivo
                    local = audio.download('mp3//')
                    # divide o caminho do diretório do arquivo separando em caminho e extensão
                    # Ex c:\users\mp3\audio.mp3 ficaria como >>> 'c:\users\mp3\audio', '.mp3'
                    diretorio, extensao = os.path.splitext(local)
                    # renomea o arquivo baixado adicionado o tipo .mp3
                    novo_destino = diretorio + '.mp3'
                    # testa se o arquivo baixado já existir
                    if novo_destino in arquivos_baixados:
                        # remove o arquivo já baixado
                        print('Sim')
                        os.remove(local)
                    else:
                        print('não')
                        # adiciona na lista as músicas baixadas
                        arquivos_baixados.append(novo_destino)
                        # troca o formato pra .mp3
                        os.renames(local, novo_destino)
                        nome_music.append(audio.title)
                        print(f'DADODADOASD = {dados}')
                        for c in dados:
                            if message.author.name in c:
                                quant_pessoas += 1
                        print(f'Quantidade de pessoas = {quant_pessoas}')
                        # adiciona em uma dict o user e em uma lista os nomes das músicas if message.author.name in user
                        pessoas[message.author.name] = nome_music[:]
                        print(pessoas.values())
                        if quant_pessoas == 0:
                            dados.append(pessoas.copy())
                            while True:
                                with open('dados\server.csv', 'a', newline='') as arquivo:
                                    add = csv.writer(arquivo)
                                    add.writerow(['User', 'Links', 'Músicas'])
                                    add.writerow(dados)
                                with open('C:/Users/andre/Documents/GitHub/botmusic/Projeto_Pythonv1/dados/server.csv',
                                          'r') as arquivo:
                                    leitor = arquivo.read()
                                    print(leitor)
                                break
                        else:
                            for d in dados:
                                for k, v in d.items():
                                    if message.author.name == k:
                                        v.append(audio.title)
                        nome_music.clear()
                        pessoas.clear()
                        quant_pessoas = 0
                        print(f'Dados = {dados}')

                    print(novo_destino[58:], "CALCINHA PRETA")
                    # envia o arquivo para o Discord
                    await message.channel.send(file=discord.File(novo_destino[58:]))
                    await message.channel.send("Protinho! :heart:")
            else:
                print(message.author)
            play = ['https://youtube.com/playlist?list=', 'https://www.youtube.com/playlist?list=']
            for dd in play:
                if dd in message.content:
                    playlist = Playlist(message.content)
                    await message.channel.send(f"Encontrei {len(playlist)} músicas!\nQuantas desejá baixar?")
                    con = str(message.content)
                    while con.isnumeric() is not True:
                        await message.channel.send('Prf didite um número!')
                    for pos, url in enumerate(playlist):
                        print('url = ', len(url))
                        video = YouTube(url)
                        audio = video.streams.filter(only_audio=True)[0]
                        destination = 'playlist//'

                        local = audio.download(output_path=destination)
                        diretorio, extensao = os.path.splitext(local)
                        novo_destino = diretorio + '.mp3'
                        diretorio, extensao = os.path.splitext(local)
                        # renomea o arquivo baixado adicionado o tipo .mp3
                        novo_destino = diretorio + '.mp3'
                        # testa se o arquivo baixado já existir
                        if novo_destino in arquivos_baixados:
                            # remove o arquivo já baixado
                            print('Sim')
                            os.remove(local)
                        else:
                            print('não')
                            # adiciona na lista as músicas baixadas
                            arquivos_baixados.append(novo_destino)
                            os.renames(local, novo_destino)
                        print(novo_destino[58:])
                        # envia o arquivo para o Discord
                        await message.channel.send(file=discord.File(novo_destino[58:]))

                    await message.channel.send("Protinho! :heart:")
        else:
            await message.channel.send(':x: Você não está na lista, infelizmente você não pode utilizar!')


# reações de emoji
@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    global pag
    fixed_channel = client.get_channel(875828784450904114)
    if user.bot:
        return
    print(f'Tamanho 3 == {len(pag)}')
    if emoji == '1️⃣':
        pag = emoji
    if emoji == '2️⃣':
        pag = emoji
    if emoji == '3️⃣':
        pag = emoji
    print(f'Tamanho 4 == {len(pag)}')


client.run("ODcyMjQyMTI2ODExOTg3OTc4.YQnAyA.UVYiwBgCF9NdUG9TIKv7jz1K2sk")
