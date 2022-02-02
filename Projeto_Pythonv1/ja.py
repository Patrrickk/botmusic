# from pytube import Playlist, YouTube
#
# playlist = Playlist('https://www.youtube.com/playlist?list=PLAsTje28QYlxlWvTcbOCua5bwUGu84obI')
#
# for url in playlist:
#     video = YouTube(url)
#     audio = video.streams.filter(only_audio=True)[0]
#     destination = 'playlist//'
#     audio.download(output_path=destination)
#     print(destination)
# print('feito')
user1 = {}
# while True:
#     list_musicas.append(str(input('nome: ')))
#     temp.append(list_musicas[:][0])
#     list_musicas.clear()
#     user['pk'] = temp
#     print(user)
# print('finalizado')
notas = []
nome_musica = list()
for c in range(0, 2):
    video = input('')
    author = 'pk'
    nome_musica.append(video)
    user1[author] = nome_musica[:]
    nome_musica.clear()
print(user1)
