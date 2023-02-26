import pygame
def width():
    info = pygame.display.Info()
    return info.current_w
def height():
    info = pygame.display.Info()
    return info.current_h
def screensize():
    return pygame.display.set_mode((width(),height()))