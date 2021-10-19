import pygame
import random
pygame.init()
import time

#hardcoding be like https://www.reddit.com/r/ProgrammerHumor/comments/9lllxu/hard_coding/
WHITE = (255,255,255)
BLACK = (0,0,0)
OUTLINE  = (255,0,0)
font = pygame.font.SysFont("freesansbold.ttf", 25)
card_font = pygame.font.SysFont("freesansbold.ttf", 250)
endS = pygame.font.SysFont("freesansbold.ttf", 150)
card_fontS = pygame.font.SysFont("freesansbold.ttf", 50)
screen = pygame.display.set_mode ((600, 600))
pygame.display.set_caption ("Card Game")

#the funtions for the text
def start(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200,300])
def end(end_score):
    screen_text = endS.render("score: " + str(score), True, WHITE)
    screen.blit(screen_text, [100,340])
def message_to_screen_1(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [0,0])
def message_to_screen_2(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [0,20])
def message_to_screen_3(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [0,40])
def message_to_screen_4(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200,470])
def message_to_screen_5(score):
    screen_text = font.render ("score: " + str(score), True, WHITE)
    screen.blit(screen_text, [500,550])
def new_cardr(card):
    screen_text = card_fontS.render ("+ " + str(card), True, OUTLINE)
    screen.blit(screen_text, [500,350])
def new_cardl(card):
    screen_text = card_fontS.render ("- " + str(card), True, OUTLINE)
    screen.blit(screen_text, [100,350])
def bottom_card(total):
    screen_text = card_font.render (str(total), True, OUTLINE)
    screen.blit(screen_text, [245,200])


start ("press C to start game", WHITE)
pygame.display.update()

#where is your god now
true = True
while true :
    #fill screen , and put text on
    screen.fill(BLACK)
    message_to_screen_4 ("stay between 1 and 21 :)" , WHITE)
    message_to_screen_1("Left Arrow = -", WHITE)
    message_to_screen_2("Right Arrow = +", WHITE)
    message_to_screen_3("Q to Quit", WHITE)


#game stuff

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    true = False

                    #minus card
                if event.key == pygame.K_LEFT:
                    message_to_screen_5 (score)
                    total = total - card
                    bottom_card(total)
                    card = random.randint(1,9)
                    new_cardl (card)
                    new_cardr (card)
                    score = score+1
                    if total > 21:
                        true = False
                    if total < 0 :
                        true = False
                    pygame.display.update()

                    #add card
                if event.key == pygame.K_RIGHT:
                    total = total + card
                    bottom_card(total)
                    message_to_screen_5 (score)
                    card = random.randint(1,9)
                    new_cardl (card)
                    new_cardr (card)
                    score = score+1
                    if total > 21:
                        true = False
                    if total < 0 :
                        true = False
                    pygame.display.update()

                    #start the game 
                if event.key == pygame.K_c: 
                    total = 9
                    card = random.randint(0,10)
                    new_cardl (card)
                    new_cardr (card)
                    bottom_card(total)
                    score = 0
                    message_to_screen_5 (score)
                    pygame.display.update()

end_score = score            
screen.fill(BLACK) 
end(end_score)      
pygame.display.update()
time.sleep (5)
pygame.quit()
