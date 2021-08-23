import json
import discord
import emoji
from random import choice

import task as task
from discord.ext import tasks
from discord.ext import commands
from random import randint, choice
from time import sleep


intents = discord.Intents.default()
intents.members = True

with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']

client = discord.Client(intents=intents)
dados = []
jogadores = {}
frase = ['Escolha, Pedra ou Papel ou tesoura']


@client.event
async def on_ready():
    print('BOT ON!')


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention
    #  previnir erro
    if author == 'TangerBOT':
        return
    while True:
        pc = choice(['pedra', 'papel', 'tesoura'])
        break
    if content == 'bom dia' and channel.name == 'bom-dia':
        await channel.send('bom dia! ' + mention)
    if content == 's2':
        await channel.send(emoji.emojize(':heart:' + mention, use_aliases=True))
    if content == 'jokenpo':
        dados.append(author)
        jogadores[author] = len(dados)
        await channel.send(f'{mention} Ok, vamos jogar, para sair basta digitar "sair"')
        sleep(.5)
    print(dados)
    print(jogadores)
    if content == 'sair':
        await channel.send(f'{mention} Você não está mais jogando!')
        dados.remove(author)
    if content == 'pedra' and author in dados[0]:  # pedra jogador
        jo = [['JO'], ['KEN'], ['PO']]
        for c in range(0, len(jo)):
            await channel.send(jo[c][0])
            sleep(1)
        await channel.send(f'{mention} escolheu PEDRA\nE eu escolhi {pc}')
        if pc == 'papel':
            await channel.send('EU VENCI')  # bot
            await channel.send(file=discord.File('imagens/uhul.gif'))
        elif pc == 'tesoura':
            await channel.send(f'{mention} VENCEU')
        elif pc == 'pedra':
            await channel.send('EMPATOU')
        else:
            await channel.send('Opcão inválida')
    elif content == 'papel' and author in dados[0]:  # papel
        jo = [['JO'], ['KEN'], ['PO']]
        for c in range(0, len(jo)):
            await channel.send(jo[c][0])
            sleep(.5)
        await channel.send(f'{mention} escolheu PAPEL\nE eu escolhi {pc}')
        if pc == 'pedra':
            await channel.send(f'{mention} VENCEU')
        elif pc == 'tesoura':
            await channel.send('EU VENCI')  # bot
            await channel.send(file=discord.File('imagens/uhul.gif'))
        elif pc == 'papel':
            await channel.send('EMPATOU')
        else:
            await channel.send('Opcão inválida')
    elif content == 'tesoura' and author in dados[0]:  # tesoura
        jo = [['JO'], ['KEN'], ['PO']]
        for c in range(0, len(jo)):
            await channel.send(jo[c][0])
            sleep(1)
        await channel.send(f'{mention} escolheu TESOURA\nE eu escolhi {pc}')
        if pc == 'pedra':
            await channel.send('EU VENCI')  # bot
            await channel.send(file=discord.File('imagens/uhul.gif'))
        elif pc == 'papel':
            await channel.send(f'{mention} VENCEU')
        elif pc == 'tesoura':
            await channel.send('EMPATOU')
        else:
            await channel.send('Opcão inválida')
    else:
        if author in dados[0]:
            await channel.send(frase[0])
        else:
            return


@client.event
async def on_member_join(member):
    channel = client.get_channel(875828784450904114)
    await channel.send(f'Obrigado por entrar! esse server é apenas para testar meu bot {member.mention}')


client.run(TOKEN)
