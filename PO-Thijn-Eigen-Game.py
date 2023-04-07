import pygame
import random
import time
import ctypes
import tkinter.messagebox
from start_menu import start_menu


# Initialize Pygame and others
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Set the screen dimensions
WINDOW_SIZE = [1280, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)

# pijlen goed laden
arrow_images = [
    pygame.image.load("Media/arrow-up.jpg"),
    pygame.image.load("Media/arrow-down.jpg"),
    pygame.image.load("Media/arrow-left.jpg"),
    pygame.image.load("Media/arrow-right.jpg")
]
# Muziek
snd_beep = pygame.mixer.Sound("Media/start_sound.mp3")

for i in range(len(arrow_images)):
    arrow_images[i] = pygame.transform.scale(arrow_images[i], WINDOW_SIZE)
selected_arrow = random.choice(arrow_images)

# variabelen
score1 = 0
score2 = 0
spelen = True
top = tkinter.Tk()
top.withdraw()
start_time = time.time()
# opmerkingen opstellen
text = "Speler 1 was sneller, de reactie tijd was "
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 108)
speler1text = font.render(text, True, (0, 0, 0))

# ----------------------- HOOFDLOOP ----------------------- #
def display_start_menu():
    font = pygame.font.Font(None, 50)
    new_game_text = font.render("Nieuw spel", True, (0, 0, 0))
    quit_text = font.render("Spel stoppen", True, (0, 0, 0))
    new_game_rect = new_game_text.get_rect(center=(640, 260))
    quit_rect = quit_text.get_rect(center=(640, 460))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if new_game_rect.collidepoint(pos):
                    game_loop()
                elif quit_rect.collidepoint(pos):
                    pygame.quit()


        screen.fill((255, 255, 255))
        screen.blit(new_game_text, new_game_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.update()

while spelen == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spelen = False
    choice = start_menu()
    if choice == "new_game":
        # Check events
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and selected_arrow == arrow_images[0]:

                score1 += 1
                if score1 == 5:
                    ctypes.windll.user32.MessageBoxW(0, u"Speler 1 heeft gewonnen!", u"Einde", 0)
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 1 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 1 was sneller!", False, (0, 0, 0)), (930, 675))
                    screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                    pygame.display.flip()
                    time.sleep(random.randint(2,5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()

            if event.key == pygame.K_DOWN and selected_arrow == arrow_images[1]:

                score1 += 1
                if score1 == 5:
                    ctypes.windll.user32.MessageBoxW(0, u"Speler 1 heeft gewonnen!", u"Einde", 0)
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 1 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 1 was sneller!", False, (0, 0, 0)), (930, 675))
                    screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                    pygame.display.flip()
                    time.sleep(random.randint(2,5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()


            if event.key == pygame.K_LEFT and selected_arrow == arrow_images[2]:

                score1 += 1
                if score1 == 5:
                    ctypes.windll.user32.MessageBoxW(0, u"Speler 1 heeft gewonnen!", u"Einde", 0)
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 1 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 1 was sneller!", False, (0, 0, 0)), (930, 675))
                    screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                    pygame.display.flip()
                    time.sleep(random.randint(2,5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()


            if event.key == pygame.K_RIGHT and selected_arrow == arrow_images[3]:
                score1 += 1

                if score1 == 5:
                    ctypes.windll.user32.MessageBoxW(0, u"Speler 1 heeft gewonnen!", u"Einde", 0)
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 1 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 1 was sneller!", False, (0, 0, 0)), (930, 675))
                    screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                    pygame.display.flip()
                    time.sleep(random.randint(2,5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()


            if event.key == pygame.K_w and selected_arrow == arrow_images[0]:

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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 2 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 2 was sneller!", False, (0, 0, 0)), (930, 675))
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 2 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 2 was sneller!", False, (0, 0, 0)), (930, 675))
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 2 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 2 was sneller!", False, (0, 0, 0)), (930, 675))
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
                    screen.blit(font.render("Reactietijd: " + str(reaction_time) + " sec", True, (0, 0, 0)), (10, 675))
                    screen.blit(font.render("Speler 2 was sneller!", True, (0, 0, 0)), (930, 675))
                    screen.blit(font.render("Score speler 1: " + str(score1), True, (0, 0, 255)), (10, 10))
                    screen.blit(font.render("Score speler 2: " + str(score2), True, (255, 0, 0)), (1000, 10))
                    pygame.display.flip()
                    time.sleep(2)
                    screen.blit(font.render("Speler 2 was sneller!", False, (0, 0, 0)), (930, 675))
                    screen.blit(font2.render("Wacht...", True, (255,0,0)), (520, 345))
                    pygame.display.flip()
                    time.sleep(random.randint(2,5))
                    selected_arrow = random.choice(arrow_images)
                    pygame.mixer.Sound.play(snd_beep)
                    start_time = time.time()


    # laat de pijl zien
    screen.blit(selected_arrow, (0, 0))
    # --- Ververs het beeldscherm --- #

    clock.tick(60)
    pygame.display.flip()

# --------------- Afsluiting -------------------#
pygame.quit()
