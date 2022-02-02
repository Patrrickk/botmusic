from time import sleep
import discord
from time import sleep
from pytube import YouTube, Playlist
import os
import emoji
import csv
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
dados = {}
https = list()
playList = https[:]
user1 = dict()
nome_musica = list()
links = {}
# Lista de quem pode utilizar o BOT
beta = [698924189431759040, 698925348473274408, 872614021977743360]
aaa = 0
podebaixar = -1
url = str()
cont = 1
ppp = 0
emoj = str()


@client.event
async def on_ready():
    print("O BOT ESTÁ ONLINE")


@client.event
async def on_message(message):
    global https, ppp, beta, number_down, id_userr, aprova, d, pk
    global playList
    global aaa, emoj
    global podebaixar
    global user1
    global nome_musica
    global links
    global cont
    global url
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention
    con = 0
    # Previnir erro
    if author == "TangerBOT":
        return
    # varri a lista beta e aprova se o user estiver nela
    for c in beta:
        id_userr = client.get_user(c)
        if id_userr == message.author:
            aprova = client.get_user(c)
    # verifica se a pessoa está na LISTA BETA
    if message.author == aprova:
        if content == "bom dia" and channel.name == "bom-dia":
            await channel.send("bom dia " + mention)
        # Lista de músicas baixadas pelo úsuario
        if content == 'músicas':
            print(f'quem olhou a LISTA FOI Author = {author} and USER1 {user1}')
            if len(user1) != 0:
                cont = 1
                for k, v in user1.items():
                    # testa se o author da msg está na lista de músicas baixadas
                    if author == k:
                        print(f'k = {k} USER1 musicas = {user1[author]}')
                        await channel.send(f'O {k} baixou {len(user1[author])} músicas')
                        for list_musicas in v:
                            number_down = await channel.send(f'{cont}: {list_musicas}')
                            cont += 1
                        emojis = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:",
                                  ":nine:",
                                  ":ten:"]
                        # envia uma reação de acordo com a quantidade de músicas
                        for c in range(0, len(links)):
                            emoj = emoji.emojize(emojis[c], use_aliases=True)
                            await number_down.add_reaction(emoj)
                await channel.send('Para baixar uma música da lista basta digitar "baixar" + número '
                                   'da música ou basta clicar na reação!')
            else:
                await channel.send('Você ainda baixou nenhuma música!')

        if author in dados:
            print('Em ppp3 = ', ppp)
            print(f'AUTHOR = {author}')
            if content == 'baixar' and len(links) > 0:
                for c in content:
                    if c.isnumeric() is True:
                        ppp = c
                        print(f'{ppp}', end='')
                print()
                print('Em ppp2 = ', ppp)
                if content == 'baixar ' + f'{ppp}':
                    print('Em ppp = ', ppp)
                    print('LINKS = ', links)
                    if ppp in links.keys():
                        print('tem')
                    else:
                        print('não tem')
        if content == 'url:':
            await channel.send('Digite a url:')
            if author not in dados:
                dados[author] = len(dados)
            podebaixar = dados[author]
            print('podebaixar=', podebaixar)
            aaa += 1
            await channel.send(f'pronto, modo download abilitado para {author}:')
            await channel.send('Você pode enviar url a qualquer momento para baixar a música')
        else:
            if aaa == 0:
                await channel.send('Para baixar músicas digite "url:"')
        # testa se é uma url valida
        valida = ['https://www.youtube.com', 'https://youtu.be/']
        # testa se é uma playlist
        valida2 = ['youtube.com/playlist']
        if valida2[0] in content:
            li = True
        else:
            li = False
        if li == True:
            await channel.send('Parece que você está tentando baixar uma PlayList! Infelizmente essa função ñ está '
                               'disponível por enquanto')
        else:
            for c in valida:
                print(f'LI é = {li}')
                if c in content and con == 0 or len(url) > 0:
                    print('EM DADOS TEMOS O SIGUINTE >>>>>', dados)
                    print(f"DADOS={dados[author]}")
                    print(f"PODE={podebaixar}")
                    https.append(str(f"'{message.content}'"))
                    playList = https[:]
                    print(f'ok con = {con} e Author {author}')
                    con += 1
                    print(f'https = {https}')
                    print(f'Quem pode baixar agora é DADOS = {dados[author]} é podebaixar = {podebaixar}')
                    if author in dados:
                        print('SIIIIIIIIIIIIIIIIIIM')
                        sleep(1)
                        await channel.send('Estou enviando, um momento')
                        if len(url) < 1:
                            url = https[0]
                        print(len(url))

                        # url do YouTube vídeo padrão
                        yt = YouTube(url)

                        # extraindo só o audio
                        video = yt.streams.filter(only_audio=True).first()

                        # verifique o destino para salvar o arquivo
                        destination = 'mp3//'

                        # baixando o arquivo
                        out_file = video.download(output_path=destination)

                        # salvando o arquevo
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        print('local', new_file)
                        title_direc = new_file[60:]
                        print('new = ', title_direc)
                        # resultado de sucesso
                        print(yt.title + ' Música baixada com sucesso')
                        nome_musica.append(video.title)
                        user1[author] = nome_musica[:]
                        co = 1
                        for cd in range(0, len(user1[author])):
                            links[co] = url
                            co += 1
                        nome_musica.clear()

                        print(f'USER {user1} and nome_musica = {nome_musica}')
                        # print(f'URL = {url}')
                        # yt = YouTube(url)
                        # yt.streams.first().download()
                        # tiltle = yt.streams.first().download()[50:]
                        # sleep(2)
                        await channel.send(file=discord.File(f'{title_direc}'))
                        await channel.send('Prontinho! :heart:')
                        # deletar arquivo baixado
                        os.remove(f'{title_direc}')
                        print('.mp3 deletado!')
                        https.clear()
                        url = ''
                    else:
                        await channel.send('Ops, parece que ocorreu um erro, tente digitar "url:" novamente, por favor')
    else:
        await channel.send(':x: Infelizmente você não está na lista de testadores BETA, mande '
                           'uma msg para o disc Pk#0616 e peça para adicionar você!')
    if content == 'g':
        print('VERDADE!')
        ddd = await channel.send('teste+++++')
        d = emoji.emojize(':two:', use_aliases=True)
        await ddd.add_reaction(d)


# reações de emoji
@client.event
async def on_reaction_add(reaction, user):
    emoji1 = reaction.emoji
    fixed_channel = client.get_channel(875828784450904114)
    global url
    if user.bot:
        return

    print(f'EMOJI = {emoji1} and emoj = {emoj}')
    if emoji1 == '1️⃣':
        playlist = Playlist('https://www.youtube.com/playlist?list=PLAsTje28QYlxlWvTcbOCua5bwUGu84obI')

        for url in playlist:
            video = YouTube(url)
            audio = video.streams.filter(only_audio=True)[0]
            destino = 'mp3//'
            audio.download(output_path=destino)

        await fixed_channel.send(file=discord.File('mp3//Como nossos pais - Belchior (Stefano Cover).mp4'))
    elif emoji1 == '2️⃣':
        print(f'Correto! {emoj}')
        await fixed_channel.send('segundo')

    # do stuff
    elif emoji1 == "3️⃣":
        await fixed_channel.send('terceiro')
    # do stuff
    else:
        return


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
