
from pytube import YouTube
import os

# url do YouTube
yt = YouTube('https://youtu.be/7xwjLCCVZRk?list=RDuVB9CAn5Np0')

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

# resultado de sucesso
print(yt.title + ' Música baixada com sucesso')
