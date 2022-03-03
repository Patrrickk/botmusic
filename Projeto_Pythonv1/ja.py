# """
# "r" -> usado somente para ler algo
# "w" -> usado somente para escrever algo
# "r+" -> usado para ler e escrever algo
# "a" -> usado acrescentar algo
# """
#
# valores = [12, 33, 55, 66]
#
# with open('valores.txt', 'w') as arquivo:
#     for valor in valores:
#         arquivo.write(str(valor) + "\n")
from pytube import Playlist, YouTube

p = Playlist(str(input("URL: ")))
print(f'Encontrei {len(p)} deseja baixar todas? por favor digite um valor: ')
quant = int(input("valor: "))
for pos, vid in enumerate(p.videos):
    if quant > pos:
        print(f'Downloading: {vid.title}')
        audio = vid.streams.filter(only_audio=True).first()
        audio.download()
print("fim")

# if quant ==
#     audio = vid.streams.filter(only_audio=True)[0]
# audio.download()