#import time
#import getch
#import twilio later
#import cvs utlity (cvs)
import pygame
import csv


pygame.init()
#set screen size
X = 800
Y = 100

bored = pygame.display.set_mode((X,Y))
# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing RGB Color
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()
#this is the colors for the players
color_player1 = (0,100,0)
color_player2 = (0,0,255)
#these are the player rectangles
#player 1
pygame.draw.rect(bored,color_player1,pygame.Rect(0,10,20,20))
pygame.draw.rect(bored,color_player2,pygame.Rect(0,30,20,20))




def endgame():
    print("endgame")

def gamerun():
    q = 0
    p = 0
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    q += 1
                if event.key == pygame.K_p:
                    p += 1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                #if q == 20:
                    #print("endgame")
                if p == 20:
                    print("p has won")
                if q == 20:
                    print("q has won")
                    pygame.quit()
            pygame.draw.rect(bored, color_player1, pygame.Rect(0, 10, 20*q, 20))
            pygame.draw.rect(bored, color_player2, pygame.Rect(0, 30, 20*p, 20))
            print(q,p)

        pygame.display.flip()
gamerun()

#data_list = [["Name", "Email"],
            #[1, "Asher", "asherforman@stu.postoakschool.org"],
            #[2, "Leila", "leilamarks@stu.postoakschool.org"],
            #[3, "Connor", "connorkissack@stu.postoakschool.org"]
            #[3, "Juan", "juancarlos@stu.postoakschool.org"]
           # [3, "Henry", "henryquillin@stu.postoakschool.org"]


   # with open('csv file', 'w', newline='') as file:
  #  writer = csv.writer(file, delimiter='|')
  #  writer.writerows(data_list)


