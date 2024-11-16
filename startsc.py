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
        return "choice"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)  # Black border with width 5
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))

class Choice(Screen):
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
    self.button1_rect = pygame.Rect((screen_width - self.button_width) // 2, screen_height // 2 - self.button_height * 2, self.button_width, self.button_height)
    self.button1_text = self.font.render("Beginner", True, (0, 0, 0))
    self.button2_rect = pygame.Rect((screen_width - (self.button_width+100)) // 2, screen_height  // 2, self.button_width+100, self.button_height)
    self.button2_text = self.font.render("Intermediate", True, (0, 0, 0))
    self.button3_rect = pygame.Rect((screen_width - self.button_width) // 2, screen_height // 2 + self.button_height * 2, self.button_width, self.button_height)
    self.button3_text = self.font.render("Pro", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button3_rect.collidepoint(event.pos):
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_image, (0, 0))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button1_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button1_rect, 5, border_radius=15)  # Black border with width 5
    pygame.draw.rect(self.screen, self.button_color, self.button2_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button2_rect, 5, border_radius=15)
    pygame.draw.rect(self.screen, self.button_color, self.button3_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button3_rect, 5, border_radius=15)
    self.screen.blit(self.button1_text, (self.button1_rect.x + (self.button_width - self.button1_text.get_width()) // 2, self.button1_rect.y + (self.button_height - self.button1_text.get_height()) // 2))
    self.screen.blit(self.button2_text, (self.button2_rect.x + (self.button_width+100 - self.button2_text.get_width()) // 2, self.button2_rect.y + (self.button_height - self.button2_text.get_height()) // 2))
    self.screen.blit(self.button3_text, (self.button3_rect.x + (self.button_width - self.button3_text.get_width()) // 2, self.button3_rect.y + (self.button_height - self.button3_text.get_height()) // 2))

test = ["Quiero ayudar a la gente.", "Nosotros trabajamos para el pueblo.", "La educación es muy importante.", "Todos tienen derechos.", "Necesitamos paz y justicia.", "La salud es nuestra prioridad.", "Trabajamos por un futuro mejor.", "Los jóvenes son el futuro.", "Queremos un país fuerte.", "Yo creo en el cambio.", "La igualdad es clave.", "Vamos a mejorar la economía.", "Es un honor servir a mi país.", "Todos merecen respeto.", "Queremos más empleos.", "Vamos a apoyar a las familias.", "La cultura es nuestra riqueza.", "Es importante escuchar a todos.", "Juntos somos más fuertes.", "Vamos a construir un mejor país.", "La seguridad es nuestra misión.", "Queremos mejorar la educación.", "Todos merecen una vida digna.", "Vamos a proteger el medio ambiente.", "La salud debe ser accesible.", "Trabajamos para el bien común.", "Vamos a construir más hospitales.", "Los niños son nuestra esperanza.", "La corrupción no es aceptable.", "Hay que cuidar a los ancianos.", "La justicia es para todos.", "Tenemos que trabajar unidos.", "Todos debemos tener una voz.", "Vamos a crear más oportunidades.", "El progreso es nuestra meta.", "Queremos más seguridad en las calles.", "La libertad es muy importante.", "Vamos a ayudar a los agricultores.", "La tecnología es el futuro.", "Tenemos un compromiso con la gente.", "Es necesario reducir la pobreza.", "Los ciudadanos son nuestra fuerza.", "La educación debe ser gratuita.", "El cambio es posible.", "Es importante cuidar nuestros recursos.", "Todos merecen un hogar seguro.", "Vamos a mejorar la infraestructura.", "La honestidad es nuestro valor.", "Necesitamos líderes responsables.", "La democracia es nuestro camino.", "Queremos mejorar nuestras ciudades.", "La educación es un derecho básico.", "La familia es la base de la sociedad.", "Los niños necesitan apoyo.", "Todos merecen una vida mejor.", "Vamos a trabajar por la justicia.", "Nuestro país necesita más oportunidades.", "Vamos a invertir en tecnología.", "Queremos mejorar el sistema de salud.", "La cultura es nuestra identidad.", "Hay que respetar la diversidad.", "Todos somos iguales.", "La paz es nuestro objetivo.", "Vamos a cuidar el medio ambiente.", "La honestidad es nuestra bandera.", "Todos debemos colaborar.", "El respeto es fundamental.", "Vamos a construir más escuelas.", "La ciencia es clave para el progreso.", "Nuestro compromiso es con la verdad.", "La transparencia es importante.", "Vamos a luchar contra la pobreza.", "Necesitamos unirnos como país.", "Todos tenemos el derecho a la libertad.", "La juventud necesita oportunidades.", "Vamos a trabajar con responsabilidad.", "Es importante proteger a los animales.", "La seguridad es nuestra prioridad.", "Vamos a crear empleos.", "El diálogo es fundamental.", "La educación abre puertas.", "Todos merecen igualdad de oportunidades.", "La naturaleza es nuestra riqueza.", "Necesitamos apoyar a las pequeñas empresas.", "Vamos a trabajar con pasión.", "El deporte une a las personas.", "Todos debemos ayudar a los demás.", "El arte nos hace mejores.", "Vamos a promover la cultura.", "Necesitamos cuidarnos unos a otros.", "La paz empieza en casa.", "Es importante pensar en el futuro.", "La educación es una inversión.", "Vamos a proteger nuestros recursos.", "La solidaridad es esencial.", "Los jóvenes tienen mucho que decir.", "Vamos a mejorar nuestras escuelas.", "Todos debemos cuidar el planeta.", "El futuro depende de nosotros.", "La unidad hace la fuerza."]
eng_trans = ["I want to help the people.", "We work for the city.", "Education is very important.", "Everyone has rights.", "We need peace and justice.", "Health is our priority.", "We work for a better future.", "Young people are the future.", "We want a strong country.", "I believe in change.", "Equality is key.", "We are going to improve the economy.", "It is an honor to serve my country.", "Everyone deserves respect.", "We want more jobs.", "We are going to support families.", "Culture is our wealth.", "It is important to listen to everyone.", "Together we are stronger.", "We are going to build a better country.", "Security is our mission.", "We want to improve education.", "Everyone deserves a dignified life.", "We are going to protect the environment.", "Health should be accessible.", "We work for the common good.", "We are going to build more hospitals.", "Children are our hope.", "Corruption is not acceptable.", "We must take care of the elderly.", "Justice is for everyone.", "We have to work together.", "Everyone should have a voice.", "We are going to create more opportunities.", "Progress is our goal.", "We want more security on the streets.", "Freedom is very important.", "We are going to help farmers.", "Technology is the future.", "We have a commitment to the people.", "It is necessary to reduce poverty.", "Citizens are our strength.", "Education should be free.", "Change is possible.", "It is important to take care of our resources.", "Everyone deserves a safe home.", "We are going to improve the infrastructure.", "Honesty is our value.", "We need responsible leaders.", "Democracy is our path.", "We want to improve our cities.", "Education is a basic right.", "The family is the foundation of society.", "Children need support.", "Everyone deserves a better life.", "We are going to work for justice.", "Our country needs more opportunities.", "We are going to invest in technology.", "We want to improve the healthcare system.", "Culture is our identity.", "We must respect diversity.", "We are all equal.", "Peace is our goal.", "We are going to care for the environment.", "Honesty is our flag.", "We must all collaborate.", "Respect is fundamental.", "We are going to build more schools.", "Science is key to progress.", "Our commitment is to the truth.", "Transparency is important.", "We are going to fight against poverty.", "We need to unite as a country.", "We all have the right to freedom.", "Youth needs opportunities.", "We are going to work with responsibility.", "It is important to protect animals.", "Security is our priority.", "We are going to create jobs.", "Dialogue is fundamental.", "Education opens doors.", "Everyone deserves equal opportunities.", "Nature is our wealth.", "We need to support small businesses.", "We are going to work with passion.", "Sports unite people.", "We must all help others.", "Art makes us better.", "We are going to promote culture.", "We need to take care of each other.", "Peace begins at home.", "It is important to think about the future.", "Education is an investment.", "We are going to protect our resources.", "Solidarity is essential.", "Young people have a lot to say.", "We are going to improve our schools.", "We must all take care of the planet.", "The future depends on us.", "Unity makes strength."]

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
          
def draw_wrapped_text(surface, text, font, color, rect):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
      # Check if adding the next word will exceed the rect width
      test_line = current_line + word + " "
      if font.size(test_line)[0] <= rect.width:
        current_line = test_line  # Word fits, add it to the line
      else:
        # Word doesn't fit, save the current line and start a new one
        lines.append(current_line)
        current_line = word + " "

    # Add the last line if there's any leftover text
    if current_line:
      lines.append(current_line)

    # Render each line
    y = rect.top
    for line in lines:
      if y + font.get_height() > rect.bottom:
        break  # Stop if we're beyond the bottom of the rect
      line_surface = font.render(line, True, color)
      surface.blit(line_surface, (rect.left, y))
      y += font.get_height()

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
    self.num = select_sent()

    self.font = pygame.font.SysFont("couriernew", 28) 
    self.font.set_bold(True)
    self.spanish = [test[self.num[0]], test[self.num[1]], test[self.num[2]], test[self.num[3]]]
    self.english = [eng_trans[self.num[0]], eng_trans[self.num[1]], eng_trans[self.num[2]], eng_trans[self.num[3]]]
    self.note_text = self.font.render(f"{self.spanish}, {self.english}", True, (0, 0, 0))

    # Timing and state control
    self.showing_initial = True
    self.showing_second = False
    self.show_after_button = False
    self.show_final_image2 = False
    self.start_time = pygame.time.get_ticks()
    self.transition_done = False

    # Button setup
    self.font1 = pygame.font.SysFont("couriernew", 48) 
    self.font1.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, screen_height - 100, self.button_width, self.button_height)
    self.button_text = self.font1.render("Next", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and not self.showing_initial and not self.showing_second:
      if self.button_rect.collidepoint(event.pos):
        self.show_after_button = True  # Start showing the first final image
        self.start_time = pygame.time.get_ticks()  # Reset timer for final image sequence

    if self.transition_done:
      return [self.spanish,self.english]

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
      self.rect = pygame.Rect(350, 150, 600, 300)
      self.rect1 = pygame.Rect(350, 350, 600, 300)
      draw_wrapped_text(self.screen, ''.join(self.spanish), self.font, (0,0,0), self.rect)
      draw_wrapped_text(self.screen, ''.join(self.english), self.font, (0,0,0), self.rect1)
      
    elif not self.show_after_button:
      # Show button with second image until button is clicked
      self.screen.blit(self.second_image, (0, 0))
      pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
      pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)
      self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
      draw_wrapped_text(self.screen, ''.join(self.spanish), self.font, (0,0,0), self.rect)
      draw_wrapped_text(self.screen, ''.join(self.english), self.font, (0,0,0), self.rect1)
     
    elif self.show_after_button:
      # Show first burn img, then switch to second after 1 second
      if not self.show_final_image2:
        if current_time - self.start_time < 500:  # final_image1 for 1 second #!!!!!!!!!!
          self.screen.blit(self.final_image1, (0, 0))
          draw_wrapped_text(self.screen, ''.join(self.spanish), self.font, (0,0,0), self.rect)
          draw_wrapped_text(self.screen, ''.join(self.english), self.font, (0,0,0), self.rect1)
        else:
          self.show_final_image2 = True  # Switch to final_image2
          self.start_time = pygame.time.get_ticks()  # Reset timer
      else:
        if current_time - self.start_time < 500:
          self.screen.blit(self.final_image2, (0, 0))  # Display final_image2
          draw_wrapped_text(self.screen, ''.join(self.spanish), self.font, (0,0,0), self.rect)
        else:
          self.transition_done = True


class MainScreen(Screen):
  def __init__(self,screen, runtime, crowd_img1, crowd_img2, crowd_img3, texts):
    super().__init__(screen)
    #images adn layers
    self.bg_image = pygame.image.load('politics/bg_main.jpeg')
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.tribuna_layer = pygame.image.load('politics/tribuna_l.png')
    self.tribuna_layer = pygame.transform.scale(self.tribuna_layer, (screen_width, screen_height))
    self.bodyguardL = pygame.image.load('politics/bodyguardL.png')
    self.bodyguardR = pygame.image.load('politics/bodyguardR.png')
    self.bodyguardR = pygame.transform.scale(self.bodyguardR, (600, 900))
    self.bodyguardL = pygame.transform.scale(self.bodyguardL, (600, 900))
    self.reaction = "neitr"
    self.pozitive = False
    self.negative = False
    #pos reactions
    self.mrhappy = pygame.image.load('politics/mrhappy.png').convert_alpha()
    self.mrhappy = pygame.transform.scale(self.mrhappy, (400, 600))
    self.mshappy = pygame.image.load('politics/mshappy.png').convert_alpha()
    self.mshappy = pygame.transform.scale(self.mshappy, (400, 600))
    self.teamo = pygame.image.load('politics/teamo.png').convert_alpha()
    self.teamo = pygame.transform.scale(self.teamo, (400, 500))
    self.loveit = pygame.image.load('politics/loveit.png').convert_alpha()
    self.loveit = pygame.transform.scale(self.loveit, (400, 500))
    #neg reactions
    self.mrfucker = pygame.image.load('politics/mrfucker.png').convert_alpha()
    self.mrfucker = pygame.transform.scale(self.mrfucker, (400, 600))
    self.sturgalvis_lamajas = pygame.image.load('politics/sturgslvis_lamajas.png').convert_alpha()
    self.sturgalvis_lamajas = pygame.transform.scale(self.sturgalvis_lamajas, (400, 600))
    self.sht = pygame.image.load('politics/sht.png').convert_alpha()
    self.sht = pygame.transform.scale(self.sht, (400, 500))

    #hinti
    self.showhint = False

    self.bodyguardL_rect = self.bodyguardL.get_rect(topleft=(-150, 150))
    self.bodyguardR_rect = self.bodyguardR.get_rect(topleft=(800, 100))
    
    self.test = texts[0]
    self.char = ""
    self.right_chars, self.speech = create_text(self.test)
    self.timer = 640
    self.hint_char = ""
    pygame.font.init()
    self.font = pygame.font.SysFont("couriernew", 25)
    self.font.set_bold(True)

    self.timer = 640
    self.clock = pygame.time.Clock()

    self.runtime = runtime
    self.speed = 200
    self.lose = False

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
      if self.bodyguardL_rect.collidepoint(event.pos) or self.bodyguardR_rect.collidepoint(event.pos):
        self.hint_char = self.right_chars[-1] if self.right_chars else ""
        self.timer -= 50
        self.showhint = True

    if self.lose:
      return "lose"
    
    if event.type == pygame.KEYDOWN:
      #give keyboard input
      if (len(event.unicode) != 0): #and (ord(event.unicode) >= 32 and ord(event.unicode) <= 126):

        self.char = event.unicode
            
        if len(self.right_chars) != 0 and self.char == self.right_chars[-1]:
          self.speech = replace_first_char("_", self.right_chars[-1], self.speech)
          self.right_chars.pop()
          self.reaction = "poz"

          self.timer += 15
          self.hint_char = ""
          self.showhint = False

          if len(self.right_chars) == 0:
            return "win"
        else:
          self.reaction = "neg"

        if event.key == pygame.K_ESCAPE:
          pygame.quit()


        if event.key == pygame.QUIT:
          pygame.quit()
          sys.exit()

  def appearance(self):
    self.runtime = pygame.time.get_ticks()
    if self.runtime % 10 == 0:  
      if self.reaction == "poz":
        self.speed = -100
        self.pozitive = True
        self.negative = False
      elif self.reaction == "neg":
        self.speed = 500
        self.pozitive = False
        self.negative = True
      self.screen.blit(self.bg_image, (0, 0))
      self.screen.blit(self.crowd_img3, (int(500 - math.sin(self.runtime/500)*10/2),int(0 - math.sin(self.runtime/(self.speed + 230))*10/2))) 
      self.screen.blit(self.crowd_img1, (int(-300 - math.sin(self.runtime/500)*10/2),int(100 - math.sin(self.runtime/(self.speed + 400))*10/2))) 
      self.screen.blit(self.crowd_img3, (int(-300 - math.sin(self.runtime/500)*10/2),int(50 - math.sin(self.runtime/(self.speed + 200))*10/2))) 
      self.screen.blit(self.crowd_img2, (int(700 - math.sin(self.runtime/500)*10/2),int(200 - math.sin(self.runtime/(self.speed + 220))*10/2)))
      if self.pozitive:
        self.screen.blit(self.mshappy, (800,50))
        self.screen.blit(self.mrhappy, (100,50))
        self.screen.blit(self.teamo, (-90, -20))
        self.screen.blit(self.loveit, (1000, -20))
      if self.negative:
        self.screen.blit(self.mrfucker, (1000,80))
        self.screen.blit(self.sturgalvis_lamajas, (50,150))
        self.screen.blit(self.sht, (900, -30))
      self.screen.blit(self.tribuna_layer, (0,0)) 
      self.screen.blit(self.politician, (265, 250))
      self.screen.blit(self.bodyguardR, (800, 100))
      self.screen.blit(self.bodyguardL, (-150, 150))
  
    #timer
    self.timer -= 0.1
    if self.timer <=0:
      self.lose = True
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

    #hint
    if self.showhint:
      pygame.draw.ellipse(self.screen, (255,255,255), Rect(60,20,150,150))
      hint_word = self.font.render("Hint:", False, (0, 0, 0))
      self.screen.blit(hint_word, (100,60))

    hint_surface = self.font.render(self.hint_char, False, (0, 0, 0))
    self.screen.blit(hint_surface, (100,100))

class Loser(Screen):
  def __init__(self, screen):
    super().__init__(screen)
    self.bg_lose = pygame.image.load('politics/booo_tomato.jpg')
    self.bg_lose = pygame.transform.scale(self.bg_lose, (screen_width, screen_height))

    self.font = pygame.font.SysFont("couriernew", 48)
    self.font.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2, self.button_width, self.button_height)
    self.button_text = self.font.render("Try again!", True, (0, 0, 0))

  def handle_events(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.button_rect.collidepoint(event.pos):
        return "game"
      
  def appearance(self):
    self.screen.blit(self.bg_lose, (0, 0))

    # Draw the button
    pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=15)
    pygame.draw.rect(self.screen, self.border_color, self.button_rect, 5, border_radius=15)  # Black border with width 5
    self.screen.blit(self.button_text, (self.button_rect.x + (self.button_width - self.button_text.get_width()) // 2, self.button_rect.y + (self.button_height - self.button_text.get_height()) // 2))
    
class Win(Screen):
  def __init__(self, screen, win_sp):
    super().__init__(screen)
    self.bg_image = pygame.image.load('politics/bg_win.jpg')
    self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
    self.font = pygame.font.SysFont("couriernew", 48)
    self.font.set_bold(True)
    self.button_width = 300
    self.button_height = 70
    self.button_color = (255,255,255)
    self.border_color = (0, 0, 0)
    self.button_rect = pygame.Rect((screen_width - self.button_width) // 2, (screen_height - self.button_height) // 2, self.button_width, self.button_height)
    self.button_text = self.font.render("Win some more!", True, (0, 0, 0))
    self.text = self.font.render(f"Your winning spree: {win_sp}", True, (0, 0, 0))

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
    self.screen.blit(self.text, (250, 100))

    