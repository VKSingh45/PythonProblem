import pygame
def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

file_path = "F:\1\1.mp3"
play_music(file_path)
