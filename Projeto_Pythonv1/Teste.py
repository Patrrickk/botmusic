from time import sleep
import pyttsx3
import pytube as pt
import moviepy.editor as mp
import pygame

engine = pyttsx3.init()
fase = 0

#  Funções
def onStart(name):
    print('staring', name)


def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)
    if name == 'fox':
        engine.say('Qual é seu nome!', 'dog')
    elif name == 'dog':
        engine.endLoop()


def falar(* msg):
    engine.say(frase[fase])


def quardar_dados(dic):
    pass


# Listas e dicionários
cores = {'red': '\033[91m',
         'green': '\033[92m',
         'yellow': '\033[93m',
         'blue': '\033[94m',
         'magenta': '\033[95m',
         'limpar': '\033[m'}

respostas = dict()
quardar_resp = list()


frase = ['''Olá sou a luisa, sou um programa de computador. Qual é seu nome?''',
         "É um prazer te conhecer", """Vou te mostrar um menu com algumas opções que estão
         disponivíes até o momento, por favor! selecione uma""",
         "Quero que você var, var toma no CUR"]
alerta = {1: 'Muito bem, basta digitar a url da música para fazer o download',
          2: 'Infelizemente essa opção ainda não está disponivel!',
          3: 'Ok, Por favor escolha um idioma',
          4: 'Não tÔ afim'}

print(len(frase))
'''RATE'''
rate = engine.getProperty('rate')  # obtendo detalhes da taxa atual de fala
print('Taxa de voz', rate)  # imprimindo a taxa de voz atual
engine.setProperty('rate', 190)  # configurando nova taxa de voz

'''VOLUME'''
volume = engine.getProperty('volume')  # conhecer o nível de volume atual (mín = 0 e máx = 1)
print('Volume da voz', volume)  # imprimindo nível de volume atual
engine.setProperty('volume', 1.0)  # configurar o nível de volume entre 0 e 1

'''VOICE'''
voices = engine.getProperty('voices')  # obtendo detalhes da voz atual
# engine.setProperty('voice', voices[0].id)  # mudar o índice, muda as vozes. 0 para homem
engine.setProperty('voice', voices[0].id)  # mudar o índice, muda as vozes. 1 para mulheres

cont = 0
# Programa Principal
while True:
    print('Fase atual', fase)
    if fase <= 3:
        cont += 1
        print('contador', cont)
        falar()
        pyttsx3.speak('')
        if fase == 0:
            respostas['nome'] = str(input('Nome: '))
            quardar_resp.append(respostas.copy())
            respostas.clear()
            quardar_dados(quardar_resp)
            fase = 1
        engine.say(quardar_resp[0]["nome"])
        if cont == 2:
            print('AQUI')
            fase = 2
            falar()
            pyttsx3.speak('')
            while True:
                pyttsx3.speak('')
                print('''
                [1] escutar música
                [2] menu de jogos
                [3] mudar voz
                [4] sair''')
                opc = int(input('Opção: '))
                if 4 >= opc > 0:
                    engine.say(alerta[opc])
                    if opc == 1:
                        pyttsx3.speak('')
                        url = str(input("URL: "))
                        print('-------→', url)
                        stream = pt.YouTube(url=url).streams.get_audio_only()
                        stream.download('mp4')
                        title = str(stream.title)

                        # conversão
                        clip = mp.AudioFileClip(f'mp4\\{title}.mp4')
                        clip.write_audiofile(f'mp3\\{title}.mp3')
                        pygame.init()

                    if opc == 3:
                        idioma = ''
                        while idioma != 'português' and idioma != 'inglês':
                            pyttsx3.speak('')
                            idioma = str(input('Mudar para inglês ou Português?')).lower().strip()
                            if idioma == 'português' or idioma == 'inglês':
                                break
                            engine.say('Erro ná digitação tente novamente')
                        if idioma == 'inglês':
                            engine.say('Mudando para inglês')
                            engine.setProperty('voice', voices[1].id)
                        if idioma == 'português':
                            engine.say('Mudando para Português')
                            engine.setProperty('voice', voices[0].id)
                else:
                    print('error')
                    engine.say('CARALHOO você é burro não é possivel? tente DE nOVO')
        if cont == 4:
            fase = 3
