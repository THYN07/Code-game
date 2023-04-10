from typing import List

import pygame
import random
import time
import ctypes
import tkinter.messagebox



# Initialiseer Pygame and andere
from pygame import Surface

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
top = tkinter.Tk()
top.withdraw()
# Set the screen dimensions
WINDOW_SIZE = [1280, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Muziek
snd_beep = pygame.mixer.Sound("Media/start_sound.mp3")

# variabelen
score1 = 0
score2 = 0
spelen = True
start_time = time.time()

# opmerkingen opstellen
text = "Speler 1 was sneller, de reactie tijd was "
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 108)
speler1text = font.render(text, True, (0, 0, 0))


# pijlen goed maken
arrow_images = [
        pygame.image.load("Media/arrow-up.jpg"),
        pygame.image.load("Media/arrow-down.jpg"),
        pygame.image.load("Media/arrow-left.jpg"),
        pygame.image.load("Media/arrow-right.jpg"),
        pygame.image.load("Media/arrow-up-fout.jpg"),
        pygame.image.load("Media/arrow-down-fout.jpg"),
        pygame.image.load("Media/arrow-left-fout.jpg"),
        pygame.image.load("Media/arrow-right-fout.jpg"),
    ]
for i in range(len(arrow_images)):
    arrow_images[i] = pygame.transform.scale(arrow_images[i], WINDOW_SIZE)



# Beginnen
pygame.mixer.music.load("Media/waiting.mp3")
pygame.mixer.music.play(-1)  # -1 means loop infinitely
screen.fill((68, 84, 107))
screen.blit(font2.render("THE ARROW GAME", True,
                        (255, 255, 255)), (285, 115))
screen.blit(font.render("Reageer zo snel mogelijk met de pijltjes of WASD", True,
                        (255, 255, 255)), (245, 345))
screen.blit(font.render("Speler 1 speelt met de pijltjes en speler 2 speelt met WASD", True,
                        (255, 255, 255)), (160, 495))
screen.blit(font.render("Vul de namen van de spelers hieronder in", True,
                        (255, 255, 255)), (290, 545))
pygame.display.flip()
naam1 = input("Naam speler 1: ")
naam2 = input("Naam speler 2: ")
info = input("typ OK als je wilt starten ")
pygame.mixer.music.stop()


selected_arrow = random.choice(arrow_images)
start_time = time.time()
pygame.display.flip()





# ----------------------- HOOFDLOOP ----------------------- #

while spelen == True:

    while start_time > 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spelen = False



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT and selected_arrow == arrow_images[4] or arrow_images[5] or arrow_images[6] or arrow_images[7]:
                    score1 -= 1
                    screen.blit(font2.render("FOUT, -1 punt voor " + naam1, True,
                                                         (255, 255, 255)), (285, 115))
                    time.sleep(5)
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()

                if event.key == pygame.K_w or pygame.K_s or pygame.K_a or pygame.K_d and selected_arrow == arrow_images[4] or arrow_images[5] or arrow_images[6] or arrow_images[7]:
                    score2 -= 1
                    screen.blit(font2.render("FOUT, -1 punt voor " + naam2, True,
                                                 (255, 255, 255)), (285, 115))
                    time.sleep(5)
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()
                else:
                    screen.blit(font2.render("Goed zo, we gaan verder...", True,
                                                 (255, 255, 255)), (285, 115))
                    time.sleep(random.randint(2, 5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()

                if event.key == pygame.K_w and selected_arrow == arrow_images[0]:
                    score2 += 1
                    if score2 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"{0} heeft gewonnen!".format(naam2), u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False
                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam2) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()

                if event.key == pygame.K_s and selected_arrow == arrow_images[1]:

                    score2 += 1
                    if score2 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"Speler 2 heeft gewonnen!", u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False
                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam2) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()


                if event.key == pygame.K_a and selected_arrow == arrow_images[2]:

                    score2 += 1
                    if score2 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"Speler 2 heeft gewonnen!", u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False
                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam2) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()

                if event.key == pygame.K_d and selected_arrow == arrow_images[3]:

                    score2 += 1
                    if score2 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"Speler 2 heeft gewonnen!", u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False
                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam2) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()

                if event.key == pygame.K_UP and selected_arrow == arrow_images[0]:

                    score1 += 1
                    if score1 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"{0} heeft gewonnen!".format(naam1), u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False

                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam1) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()

                if event.key == pygame.K_DOWN and selected_arrow == arrow_images[1]:

                    score1 += 1
                    if score1 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"{0} heeft gewonnen!".format(naam1), u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False


                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam1) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()


                if event.key == pygame.K_LEFT and selected_arrow == arrow_images[2]:

                    score1 += 1
                    if score1 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"{0} heeft gewonnen!".format(naam1), u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False

                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam1) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()


                if event.key == pygame.K_RIGHT and selected_arrow == arrow_images[3]:
                    score1 += 1

                    if score1 == 5:
                        ctypes.windll.user32.MessageBoxW(0, u"{0} heeft gewonnen!".format(naam1), u"Einde", 0)
                        opnieuwBeginnen = tkinter.messagebox.askquestion("Einde spel", "Wil je opnieuw beginnen?")
                        if opnieuwBeginnen == 'yes':
                            score1 = 0
                            score2 = 0
                            time.sleep(random.randint(2, 5))
                            selected_arrow = random.choice(arrow_images)
                            pygame.mixer.Sound.play(snd_beep)
                            start_time = time.time()
                            pygame.display.flip()
                            pygame.display.set_mode(WINDOW_SIZE)
                        if opnieuwBeginnen == 'no':
                            spelen = False
                    else:
                        reaction_time = (time.time() - start_time)
                        reaction_time = round(reaction_time, 2)
                        screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (255, 255, 255)), (10, 675))
                        screen.blit(font.render(str(naam1) + " was sneller!", True, (255, 255, 255)), (930, 675))
                        screen.blit(font.render("Score " + str(naam1) + ": " + str(score1), True, (0, 0, 255)), (10, 10))
                        screen.blit(font.render("Score " + str(naam2) + ": " + str(score2), True, (255, 0, 0)), (1000, 10))
                        pygame.display.flip()
                        time.sleep(2)
                        screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                        pygame.display.flip()
                        time.sleep(random.randint(2,5))
                        selected_arrow = random.choice(arrow_images)
                        pygame.mixer.Sound.play(snd_beep)
                        start_time = time.time()


    else:
        selected_arrow = random.choice(arrow_images)
        pygame.mixer.Sound.play(snd_beep)
        start_time = time.time()




    screen.blit(selected_arrow, (0, 0))
    # --- Ververs het beeldscherm --- #

    clock.tick(60)
    pygame.display.flip()




# --------------- Afsluiting -------------------#
pygame.quit()
