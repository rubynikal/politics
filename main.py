import pygame
from pygame.locals import *
import sys
from startsc import StartScreen, SecondScreen
 
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

current_screen = StartScreen(screen)  # Start with the beginning screen
running = True

while running:
  for event in pygame.event.get():
    next_screen = current_screen.handle_events(event)
    if next_screen == "game":
      current_screen = SecondScreen(screen)
    elif next_screen == "game2":
      pass  # Switch to the game screen

  current_screen.appearance()  # Draw the current screen
  current_screen.update()  # Update the display


    