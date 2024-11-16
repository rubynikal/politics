import pygame
from pygame.locals import *
import sys
import random
import math

surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

color = (0,0,0)
#pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))

letter = ""
arr_text_ = ""
right_letters = []
timer = 640
hint = ""

def create_sent():
    arr_text = ["Despite", "the", "torrential", "downpour", "that", "began", "unexpectedly", "and",
    "caught", "many", "unprepared", "Sarah,", "who", "had", "been", "eagerly", 
    "anticipating", "this", "day", "for", "weeks", "carefully", "navigated"]
    right_letters = []
    arr_text_ = ""
    for i in range(len(arr_text)):

        if random.randint(0,1) < 21:
            for c in range(1):
                a = random.randint(0, len(arr_text[i])-1)
                if arr_text[i][a] != "□":
                    b = list(arr_text[i])
                    right_letters.append(b[a])
                    b[a] = "□"
                    arr_text[i] = "".join(b)
        else:
            for c in range(len(arr_text[i])):
                b = list(arr_text[i])
                right_letters.append(b[c])
                b[c] = "□"
                arr_text[i] = "".join(b)
 
    right_letters = right_letters[::-1]

    a = 0
    for i in arr_text:
        arr_text_ += i + " "
        if a > 3:
            arr_text_ += "/"
            a = 0
        a += 1

    return right_letters, arr_text_

right_letters, arr_text_ = create_sent()
print(arr_text_)

def replace_first(chr1,chr2,str):
    str = list(str)
    for i in range(len(str)):
        if str[i] == chr1:
            str[i] = chr2
            str = "".join(str)
            return str

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)

while True:
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (len(event.unicode) != 0) and (ord(event.unicode) >= 32 and ord(event.unicode) <= 126):

                letter = event.unicode
                
                if len(right_letters) != 0 and letter == right_letters[-1]:
                    arr_text_ = replace_first("□", right_letters[-1], arr_text_)
                    right_letters.pop()
                    print(arr_text_)
                    timer += 15
                    hint = ""

                if len(right_letters) == 0:
                    right_letters, arr_text_ = create_sent()



            if event.key == pygame.K_BACKSPACE:
                timer += 50

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_SPACE:
                hint = right_letters[-1]
                timer -= 50

            if event.key == pygame.QUIT:
                pygame.quit()
                sys.exit()



    timer -= 0.1
    timer = min(timer,640)
    timer = max(timer,0)
    pygame.draw.rect(surface, (int(255*(1-timer/640)),int(255*(timer/640)),0), Rect(320,80,timer,10))


    clock.tick()
    runtime = pygame.time.get_ticks()

    pygame.draw.ellipse(surface, (255,255,255), Rect(365,270,550,250))
    pygame.draw.ellipse(surface, (255,255,255), Rect(590-math.sin(runtime/500)*10/2,500-math.sin(runtime/500)*10/2,100+math.sin(runtime/500)*10,100+math.sin(runtime/500)*10))

    text_surface = []
    anc = 0

    for i in range(len(arr_text_)):
        if arr_text_[i] == "/":
           text_surface.append(my_font.render(arr_text_[anc:i-1], False, (0, 255, 0)))
           anc = i+1

    text_surface.append(my_font.render(arr_text_[anc:-1], False, (0, 255, 0)))

    letter_surface = my_font.render(letter, False, (0, 255, 0))
    fps_surface = my_font.render(str(clock.get_fps()), False, (0, 255, 0))
    hint_surface = my_font.render(hint, False, (0, 255, 0))

    for i in range(len(text_surface)):
        surface.blit(text_surface[i], (450,320+i*20))
    
    surface.blit(letter_surface, (635,530))
    surface.blit(fps_surface, (10,10))
    surface.blit(hint_surface, (100,100))

    pygame.display.flip()
