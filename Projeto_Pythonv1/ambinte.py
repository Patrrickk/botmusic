
from pytube import YouTube, Playlist
import os

# url do YouTube
yt = YouTube('https://youtu.be/7xwjLCCVZRk?list=RDuVB9CAn5Np0')
playlist = Playlist('https://www.youtube.com/playlist?list=PLAsTje28QYlwsrrLhzuDuJGr9rrDqw8cK')
# extraindo só o audio
for url in playlist:
video = yt.streams.filter(only_audio=True).first()

# verifique o destino para salvar o arquivo
destination = 'mp3//'

# baixando o arquivo
out_file = video.download(output_path=destination)

# salvando o arquevo
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# resultado de sucesso
print(yt.title + ' Música baixada com sucesso')
