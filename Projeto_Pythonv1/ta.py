import discord
from pytube import YouTube


def progress_func(args):
    pass


yt = YouTube(
    'https://youtu.be/YW4-V0xQkTg?list=RDYW4-V0xQkTg',
    on_progress_callback=progress_func,
)
stream = yt.streams.filter(only_audio=True).first()
stream.download()
