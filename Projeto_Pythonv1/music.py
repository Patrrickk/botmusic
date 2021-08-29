import pygame
from time import sleep

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('mp3/Sultans Of Swing Solo - Dire Straits - Acoustic Guitar Cover.mp3')
pygame.mixer.music.play()
print('GET_ENDE =', pygame.mixer.music.get_endevent())

musica_end = pygame.USEREVENT+1
print(musica_end)
pygame.mixer.music.set_endevent(musica_end)


def envet_music():
    pygame.mixer.music.set_endevent(1)


while True:
    if pygame.mixer.music.get_busy() is not True:
        pass
    if pygame.mixer.music.get_pos() == -1:
        pygame.mixer.music.stop()
        break

# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() is not True:
#     print(pygame.mixer.music.get_pos())
#     pass

