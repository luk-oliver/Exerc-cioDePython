import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input()   # só funcionou por causa do input(), sem ele não roda
pygame.event.wait()




