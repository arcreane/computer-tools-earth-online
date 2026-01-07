import pygame

def Image(path):
    return pygame.image.load(path)

def Sound(path):
    return pygame.mixer.Sound(path)

def Font(path, size):
    return pygame.font.Font(path, size)
