import pygame
from pygame.locals import *
import sys
import math
import random

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
    self.bg_image = pygame.image.load('politics/start.jpg')
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.font = pygame.font.SysFont("couriernew", 48)
    self.font.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2 + 100, self.button_width, self.button_height)
    self.button_text = self.font.render("Start", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button_rect.collidepoint(event.pos):
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)  # Black border with width 5
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))

class SecondScreen(Screen):
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
    self.transition_done = False

    # Button setup
    self.font = pygame.font.SysFont("couriernew", 48) 
    self.font.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, screen_height - 100, self.button_width, self.button_height)
    self.button_text = self.font.render("Next", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and not self.showing_initial and not self.showing_second:
      if self.button_rect.collidepoint(event.pos):
        self.show_after_button = True  # Start showing the first final image
        self.start_time = pygame.time.get_ticks()  # Reset timer for final image sequence

    if self.transition_done:
      return "game2"

  def appearance(self):
    # Check timing to control image display
    current_time = pygame.time.get_ticks()
        
    if self.showing_initial and current_time - self.start_time >= 10000:  # 5 seconds for initial img
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
      pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
      pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)
      self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
      
        
    elif self.show_after_button:
      # Show first burn img, then switch to second after 1 second
      if not self.show_final_image2:
        if current_time - self.start_time < 500:  # final_image1 for 1 second #!!!!!!!!!!
          self.screen.blit(self.final_image1, (0, 0))
        else:
          self.show_final_image2 = True  # Switch to final_image2
          self.start_time = pygame.time.get_ticks()  # Reset timer
      else:
        if current_time - self.start_time < 500:
          self.screen.blit(self.final_image2, (0, 0))  # Display final_image2
        else:
          self.transition_done = True

def select_sent():
  numuri =[]
  while True:
    sk = random.randint(0, 99)
    if sk not in numuri:
      numuri.append(sk)
    if len(numuri) >= 4:
      break
  return numuri
          
def create_text(text): #hide chars from text
  right_chars = []

  for i in range(len(text)):
    last_char = 0
    for iteration in range(int(len(text[i]))):
      rand_char = random.randint(0, len(text[i])-1)
      if rand_char > last_char and text[i][rand_char] != "_":
        if text[i][rand_char] != ",":
          if text[i][rand_char] != ".":
            if text[i][rand_char] != " ":
              text_copy = list(text[i])
              right_chars.append(text_copy[rand_char])
              text_copy[rand_char] = "_"
              text[i] = "".join(text_copy)
              last_char = rand_char

  right_chars = right_chars[::-1]
  return right_chars, text  

def replace_first_char(chr1,chr2,arr):
    for i in range(len(arr)):
        sente = list(arr[i])
        for a in range(len(sente)):
          if sente[a] == chr1:
              sente[a] = chr2
              arr[i] = "".join(sente)
              return arr


class MainScreen(Screen):
  def __init__(self,screen, runtime, crowd_img1, crowd_img2, crowd_img3):
    super().__init__(screen)
    #images adn layers
    self.bg_image = pygame.image.load('politics/bg_main.jpeg')
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.tribuna_layer = pygame.image.load('politics/tribuna_l.png')
    self.tribuna_layer = pygame.transform.scale(self.tribuna_layer, (screen_width, screen_height))

    self.test = ["Quiero ayudar a la gente.", "Nosotros trabajamos para el pueblo.", "La educación es muy importante.", "Todos tienen derechos.", "Necesitamos paz y justicia.", "La salud es nuestra prioridad.", "Trabajamos por un futuro mejor.", "Los jóvenes son el futuro.", "Queremos un país fuerte.", "Yo creo en el cambio.", "La igualdad es clave.", "Vamos a mejorar la economía.", "Es un honor servir a mi país.", "Todos merecen respeto.", "Queremos más empleos.", "Vamos a apoyar a las familias.", "La cultura es nuestra riqueza.", "Es importante escuchar a todos.", "Juntos somos más fuertes.", "Vamos a construir un mejor país.", "La seguridad es nuestra misión.", "Queremos mejorar la educación.", "Todos merecen una vida digna.", "Vamos a proteger el medio ambiente.", "La salud debe ser accesible.", "Trabajamos para el bien común.", "Vamos a construir más hospitales.", "Los niños son nuestra esperanza.", "La corrupción no es aceptable.", "Hay que cuidar a los ancianos.", "La justicia es para todos.", "Tenemos que trabajar unidos.", "Todos debemos tener una voz.", "Vamos a crear más oportunidades.", "El progreso es nuestra meta.", "Queremos más seguridad en las calles.", "La libertad es muy importante.", "Vamos a ayudar a los agricultores.", "La tecnología es el futuro.", "Tenemos un compromiso con la gente.", "Es necesario reducir la pobreza.", "Los ciudadanos son nuestra fuerza.", "La educación debe ser gratuita.", "El cambio es posible.", "Es importante cuidar nuestros recursos.", "Todos merecen un hogar seguro.", "Vamos a mejorar la infraestructura.", "La honestidad es nuestro valor.", "Necesitamos líderes responsables.", "La democracia es nuestro camino.", "Queremos mejorar nuestras ciudades.", "La educación es un derecho básico.", "La familia es la base de la sociedad.", "Los niños necesitan apoyo.", "Todos merecen una vida mejor.", "Vamos a trabajar por la justicia.", "Nuestro país necesita más oportunidades.", "Vamos a invertir en tecnología.", "Queremos mejorar el sistema de salud.", "La cultura es nuestra identidad.", "Hay que respetar la diversidad.", "Todos somos iguales.", "La paz es nuestro objetivo.", "Vamos a cuidar el medio ambiente.", "La honestidad es nuestra bandera.", "Todos debemos colaborar.", "El respeto es fundamental.", "Vamos a construir más escuelas.", "La ciencia es clave para el progreso.", "Nuestro compromiso es con la verdad.", "La transparencia es importante.", "Vamos a luchar contra la pobreza.", "Necesitamos unirnos como país.", "Todos tenemos el derecho a la libertad.", "La juventud necesita oportunidades.", "Vamos a trabajar con responsabilidad.", "Es importante proteger a los animales.", "La seguridad es nuestra prioridad.", "Vamos a crear empleos.", "El diálogo es fundamental.", "La educación abre puertas.", "Todos merecen igualdad de oportunidades.", "La naturaleza es nuestra riqueza.", "Necesitamos apoyar a las pequeñas empresas.", "Vamos a trabajar con pasión.", "El deporte une a las personas.", "Todos debemos ayudar a los demás.", "El arte nos hace mejores.", "Vamos a promover la cultura.", "Necesitamos cuidarnos unos a otros.", "La paz empieza en casa.", "Es importante pensar en el futuro.", "La educación es una inversión.", "Vamos a proteger nuestros recursos.", "La solidaridad es esencial.", "Los jóvenes tienen mucho que decir.", "Vamos a mejorar nuestras escuelas.", "Todos debemos cuidar el planeta.", "El futuro depende de nosotros.", "La unidad hace la fuerza."]
    self.test = self.test[0:4]
    self.char = ""
    self.right_chars, self.speech = create_text(self.test)
    print(self.right_chars, self.speech)
    self.timer = 640
    self.hint_char = ""
    pygame.font.init()
    self.font = pygame.font.SysFont("couriernew", 25)
    self.font.set_bold(True)

    self.timer = 640
    self.clock = pygame.time.Clock()

    self.runtime = runtime
    self.speed = 200

    self.crowd_img1 = crowd_img1
    self.crowd_img2 = crowd_img2
    self.crowd_img3 = crowd_img3
    self.politician = pygame.image.load('politics/politicianw.png')
    self.politician = pygame.transform.scale(self.politician, (750,850))
    

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      return "game3"
    
    if self.timer <= 0:
      return "lose"
    
    if event.type == pygame.KEYDOWN:
      #give keyboard input
      if (len(event.unicode) != 0): #and (ord(event.unicode) >= 32 and ord(event.unicode) <= 126):

        self.char = event.unicode
            
        if len(self.right_chars) != 0 and self.char == self.right_chars[-1]:
          self.speech = replace_first_char("_", self.right_chars[-1], self.speech)
          self.right_chars.pop()

          self.timer += 15
          self.hint_char = ""

          if len(self.right_chars) == 0:
            self.right_chars, self.speech = create_text(self.test)


        if event.key == pygame.K_ESCAPE:
          pygame.quit()

        #get hint
        if event.key == pygame.K_SPACE:
          self.hint_char = self.right_chars[-1]
          self.timer -= 50

        if event.key == pygame.QUIT:
          pygame.quit()
          sys.exit()


        
  def appearance(self):
    self.runtime = pygame.time.get_ticks()
    if self.runtime % 10 == 0:  
      self.screen.blit(self.bg_image, (0, 0))
      self.screen.blit(self.crowd_img3, (int(500 - math.sin(self.runtime/500)*10/2),int(0 - math.sin(self.runtime/(self.speed + 230))*10/2))) 
      self.screen.blit(self.crowd_img1, (int(-300 - math.sin(self.runtime/500)*10/2),int(100 - math.sin(self.runtime/(self.speed + 400))*10/2))) 
      self.screen.blit(self.crowd_img3, (int(-300 - math.sin(self.runtime/500)*10/2),int(50 - math.sin(self.runtime/(self.speed + 200))*10/2))) 
      self.screen.blit(self.crowd_img2, (int(700 - math.sin(self.runtime/500)*10/2),int(200 - math.sin(self.runtime/(self.speed + 220))*10/2)))
      self.screen.blit(self.tribuna_layer, (0,0)) 
      self.screen.blit(self.politician, (265, 250))


    #timer
    self.timer -= 0.1
    self.timer = min(self.timer,640)
    self.timer = max(self.timer,0)
    pygame.draw.rect(self.screen, (255,255,255), Rect(320,80,640,10))
    pygame.draw.rect(self.screen, (int(255*(1-self.timer/640)),int(255*(self.timer/640)),0), Rect(320,80,self.timer,10))


    #thoughts
    pygame.draw.ellipse(self.screen, (255,255,255), Rect(365,150,600,250))
    pygame.draw.ellipse(self.screen, (255,255,255), Rect(590-math.sin(self.runtime/500)*10/2,370-math.sin(self.runtime/500)*10/2,100+math.sin(self.runtime/500)*10,100+math.sin(self.runtime/500)*10))

    #text
    text_surface = []
    for i in range(len(self.speech)):
      text_surface.append(self.font.render(str(self.speech[i]), False, (0, 0, 0)))
    for i in range(len(text_surface)):
      self.screen.blit(text_surface[i], (420,200+i*40))

    #char
    char_surface = self.font.render(self.char, False, (0, 0, 0))
    self.screen.blit(char_surface, (630,410))

    #fps
    hint_surface = self.font.render(self.hint_char, False, (0, 0, 0))
    self.screen.blit(hint_surface, (100,100))

class Loser(Screen):
  def __init__(self, screen):
    super().__init__(screen)
    self.bg_image = pygame.image.load('politics/lose.jpg')
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.font = pygame.font.SysFont("couriernew", 48)
    self.font.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2 + 100, self.button_width, self.button_height)
    self.button_text = self.font.render("Try again!", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button_rect.collidepoint(event.pos):
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)  # Black border with width 5
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
    