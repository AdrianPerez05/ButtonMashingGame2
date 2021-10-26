import time
import getch
from tkinter import *
import pygame

def gamefun():
    high_score = 0
    istancde = 0
    name = "Button Mashing Race"
    while True:
        distance = int(0)
        print('\n--------------------------------------------------------------')
        print('\n\nWelcome to the 100m sprint, tap z and x rapidly to move!')
        print('* = 10m')
        print('\nCurrent record:' + str(high_score) + ' by: ' + name)
        print('\nPress enter to start')
        input()
        print('Ready...')
        time.sleep(1)
        print('GO!')
        start_time = time.time()

        import pygame
        x = 0
        z = 0
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        x += 1
                    if event.key == pygame.K_z:
                        z += 1
            print(x, "   vs    ", z)

            timeout = 5

        t = Timer(timeout, print, ['Sorry, times up'])
        t.start()
        prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        answer = input(prompt)

        t.cancel()

        fin_time = time.time() - start_time
        fin_time = round(fin_time, 2)

        print('Congratulations on successfully completing the race!')
        print('You took', fin_time, 'seconds to reach the finish line')

        if fin_time < high_score:
            print("Well done you've got a new high score ")
            name = input("Please enter your name : ")
            high_score = fin_time
gamefun()
