import pygame
from pygame.locals import *
import sys
from startsc import StartScreen, SecondScreen, MainScreen, Loser, Choice, Win
import random
 
#postojannoe
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
screen_width = 1280 
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height)) 
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

pygame.display.set_caption("Politics game")

crowd_img1 = pygame.image.load('politics/crowd_img1.png').convert_alpha()
crowd_img1 = pygame.transform.scale(crowd_img1, (1110,762))
crowd_img2 = pygame.image.load('politics/crowd_img2.png').convert_alpha()
crowd_img2 = pygame.transform.scale(crowd_img2, (1110,762))
crowd_img3 = pygame.image.load('politics/crowd_img3.png').convert_alpha()
crowd_img3 = pygame.transform.scale(crowd_img3, (1110,762))
    

current_screen = StartScreen(screen) # Start with the beginning screen
running = True
winning_score = 0
while running:
  runtime = pygame.time.get_ticks()
  for event in pygame.event.get():
    next_screen = current_screen.handle_events(event)
    if next_screen == "choice":
      current_screen = Choice(screen)
    elif next_screen == "game":
      current_screen = SecondScreen(screen)
    elif isinstance(next_screen, list):
      current_screen =  MainScreen(screen, runtime, crowd_img1, crowd_img2, crowd_img3, next_screen)
    elif next_screen == "lose":
      current_screen = Loser(screen)
    elif next_screen == "win":
      winning_score = int(current_screen.timer)
      current_screen = Win(screen, winning_score)

  current_screen.appearance()  # Draw the current screen
  current_screen.update()  # Update the display


    
