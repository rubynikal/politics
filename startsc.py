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
        return "game2"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))
    self.screen.blit(self.text, ((screen_width - self.text.get_width()) // 2, screen_height // 4))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect)
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
    
class ThirdScreen(Screen):
  def __init__(self, screen):
    super().__init__(screen)
    # Load images
    self.initial_image = pygame.image.load('politics/initial.jpg')
    self.initial_image = pygame.transform.scale(self.initial_image, (screen_width, screen_height))
    self.second_image = pygame.image.load('politics/second.jpg')
    self.second_image = pygame.transform.scale(self.second_image, (screen_width, screen_height))
    self.final_image1 = pygame.image.load('politics/burn1.jpg')
    self.final_image1 = pygame.transform.scale(self.final_image1, (screen_width, screen_height))
    self.final_image2 = pygame.image.load('politics/burn2.jpg')
    self.final_image2 = pygame.transform.scale(self.final_image2, (screen_width, screen_height))

    # Timing and state control
    self.showing_initial = True
    self.showing_second = False
    self.show_after_button = False
    self.show_final_image2 = False
    self.start_time = pygame.time.get_ticks()

    # Button setup
    self.button_width = 200
    self.button_height = 50
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, screen_height - 100, self.button_width, self.button_height)
    self.button_text = pygame.font.Font(None, 50).render("Next", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and not self.showing_initial and not self.showing_second:
      if self.button_rect.collidepoint(event.pos):
        self.show_after_button = True  # Start showing the first final image
        self.start_time = pygame.time.get_ticks()  # Reset timer for final image sequence

  def appearance(self):
    # Check timing to control image display
    current_time = pygame.time.get_ticks()
        
    if self.showing_initial and current_time - self.start_time >= 5000:  # 5 seconds for initial img
      self.showing_initial = False
      self.showing_second = True
      self.start_time = pygame.time.get_ticks()

    elif self.showing_second and current_time - self.start_time >= 5000:  # 5 seconds for second img
      self.showing_second = False  # Prepare for button to appear

      # Display images based on state
    if self.showing_initial:
      self.screen.blit(self.initial_image, (0, 0))
        
    elif self.showing_second:
      self.screen.blit(self.second_image, (0, 0))
        
    elif not self.show_after_button:
      # Show button with second image until button is clicked
      self.screen.blit(self.second_image, (0, 0))
      pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)
      self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
        
    elif self.show_after_button:
      # show first burn img then switch to second after 1 sec
      if not self.show_final_image2:
        if current_time - self.start_time < 1000:  # Show final_image1 for 5 seconds
          self.screen.blit(self.final_image1, (0, 0))
        else:
          self.show_final_image2 = True  # Switch to final_image2
          self.start_time = pygame.time.get_ticks()  # Reset timer
      else:
        self.screen.blit(self.final_image2, (0, 0))  # Show final_image2
          
