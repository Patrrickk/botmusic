# from pytube import Playlist, YouTube
#
# playlist = Playlist('https://www.youtube.com/playlist?list=PLAsTje28QYlxlWvTcbOCua5bwUGu84obI')
#
# for url in playlist:
#     video = YouTube(url)
#     audio = video.streams.filter(only_audio=True)[0]
#     destination = 'mp3//'
#     audio.download(output_path=destination)
#     print(destination)
# print('feito')
playlist = ['https://www.youtube.com/playlist?list=PLAsTje28QYlxlWvTcbOCua5bwUGu84obI']
if playlist[0].find('playlist'):
    print('OK')
else:
    print('OK2')
if 'youtube.com/playlist' in playlist[0]:
    li = True
    print('VERDADE')
else:
    print('MENTIRA')
    li = False
print(li)

