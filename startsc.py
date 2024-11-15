import pygame
from pygame.locals import *
import sys

FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Start Screen")

screen_width = 1280 
screen_height = 720

class Screen:
  def __init__(self, screen):
    self.screen = screen

  def handle_events(self, event):
    pass

  def appearance(self):
    pass

  def update(self):
    pygame.display.flip()

class StartScreen(Screen):
  def __init__(self, screen):
    super().__init__(screen)
    self.bg_image = pygame.image.load('politics/bg1.jpg')  
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.font = pygame.font.Font(None, 88) 
    self.text = self.font.render("Welcome to the Game!", True, (255, 255, 255))
    self.button_width = 200
    self.button_height = 50
    self.button_color = (0,255,0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2 + 100, self.button_width, self.button_height)
    self.button_text = self.font.render("Start", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button_rect.collidepoint(event.pos):
        print("game")
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))
    self.screen.blit(self.text, ((screen_width - self.text.get_width()) // 2, screen_height // 4))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect)
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
    
class SecondScreen(Screen):
  def __init__(self, screen):
    super().__init__(screen)
    self.bg_image = pygame.image.load('politics/bg1.jpg')  
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.font = pygame.font.Font(None, 88) 
    self.text = self.font.render("Welcome to the Game!", True, (255, 255, 255))
    self.button_width = 200
    self.button_height = 50
    self.button_color = (0,255,0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2 + 100, self.button_width, self.button_height)
    self.button_text = self.font.render("Start", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button_rect.collidepoint(event.pos):
        print("game")
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))
    self.screen.blit(self.text, ((screen_width - self.text.get_width()) // 2, screen_height // 4))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect)
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
    
class SecondScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.initial_image = pygame.image.load('politics/initial.jpg')
        self.initial_image = pygame.transform.scale(self.initial_image, (screen_width, screen_height))
        self.second_image = pygame.image.load('politics/second.jpg')
        self.second_image = pygame.transform.scale(self.second_image, (screen_width, screen_height))

        self.showing_initial = True
        self.start_time = pygame.time.get_ticks()
        
        # Button
        self.button_width = 200
        self.button_height = 50
        self.button_rect = pygame.Rect(1000, 600, self.button_width, self.button_height)
        self.button_text = pygame.font.Font(None, 50).render("Next", True, (0, 0, 0))  # Black button text

    def handle_events(self, event):
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if not self.showing_initial and event.type == pygame.MOUSEBUTTONDOWN:
        if self.button_rect.collidepoint(event.pos):
          return "game2" 

    def appearance(self):
      #check time to switch images
      current_time = pygame.time.get_ticks()
      if self.showing_initial and current_time - self.start_time >= 5000: 
        self.showing_initial = False  

      #image
      if self.showing_initial:
        self.screen.blit(self.initial_image, (0, 0))  #initial image
      else:
        self.screen.blit(self.second_image, (0, 0))  #second image
        pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)  # Button with green color
        self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))