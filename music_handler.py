import pygame
import sys, os


def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return path


def play_background_music():
    pygame.mixer.music.load(resource_path("sound/background_music.mp3"))
    pygame.mixer.music.play(-1)


def play_env_sounds():
    sun_sound = pygame.mixer.Sound(resource_path("sound/sun_sound.mp3"))
    sun_sound.set_volume(0.2)
    sun_sound.play()
