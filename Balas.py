import time
from pygame.locals import *
import pygame

from gaem import BLACK

guanyador = 0
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
WHITE = (255,255,255)
BLUE = (0,0,255)
VERMEL= (255,0,0)
GOLD= (220,160,15)
# pantalles:
# pantalla 1 = menú
# pantalla 2 = credits
# pantalla 3 = joc
# pantalla 4 = game over
pantalla_actual = 1


# Vides jugador1

vides_image1 = pygame.image.load("assets/vides_image1.png")
vides_image2 =pygame.image.load("assets/vides_image2.png")

# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 5
vides_jugador1 = 3


# Jugador 2:
player_image2 = pygame.image.load('assets/nau2.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 5
vides_jugador2 = 3

# Bala rectangular blanca:
bala_imatge1 = pygame.image.load("assets/bala1.png") #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge2 = pygame.image.load("assets/bala2.png")
# bala_imatge.fill(BLUE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 10
temps_entre_bales = 500 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("MONKEY SPACE")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
def mostra_menu():
    # Mostrar imatge de fons del menú
    imprimir_pantalla_fons("assets/fons_inici.png")
    font1 = pygame.font.SysFont(None,80 )
    font2 = pygame.font.SysFont(None,60)
    imag1 = font1.render("Monkey Space ",True,GOLD)
    imag2 = font2.render("1. Jugar ", True, GOLD)
    imag3 = font2.render("2. Crèdits ", True, GOLD)
    imag4 = font2.render("3. Sortir ", True, GOLD)
    pantalla.blit(imag1,(200, 100))
    pantalla.blit(imag2, (270, 200))
    pantalla.blit(imag3, (270, 300))
    pantalla.blit(imag4, (270, 400))
    pygame.init()
    ambient_music = pygame.mixer.Sound('assets/SonidoFondo.mp3')
    ambient_music.play()



def mostra_credits():
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def mostra_credits():
     # Mostrar imatge de fons del menú
    imprimir_pantalla_fons("assets/credits.png")
    font1 = pygame.font.SysFont(None, 70)
    font2 = pygame.font.SysFont(None, 50)
    imag11 = font1.render("Credits ", True, BLUE)
    imag12 = font2.render("Programació = David Tulvan", True, BLUE)
    imag13 = font2.render("Grafics = David Tulvan", True, BLUE)
    imag14 = font2.render("Musica =", True, BLUE)
    imag15 = font2.render("Efectes Especials =", True, BLUE)
    pantalla.blit(imag11, (200, 50))
    pantalla.blit(imag12, (200, 150))
    pantalla.blit(imag13, (200, 250))
    pantalla.blit(imag14, (200, 350))
    pantalla.blit(imag15, (200, 450))
while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
     # Pantalla de Crèdit
        if pantalla_actual == 4:
            # Restauro vidas
            vides_jugador2 =3
            vides_jugador1 = 3
            # elimino les bales del joc
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                        pantalla_actual = 1
        # Pantalla de Crèdit
        if pantalla_actual == 2:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1


        #     pANTALLA de menú
        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_1:
                    ambient_music = pygame.mixer.Sound('assets/SonidoFondo.mp3')
                    ambient_music.play()
                    pantalla_actual = 3
                if event.key == K_2:
                    pantalla_actual = 2
                if event.key == K_3:
                    pygame.quit()
        # controlar trets de les naus
        if pantalla_actual == 3:
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                    pygame.init()
                    ambient_music = pygame.mixer.Sound('assets/Sonidobala1.wav')
                    ambient_music.play()
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                    pygame.init()
                    ambient_music = pygame.mixer.Sound('assets/sonidobala2.wav')
                    ambient_music.play()


    if pantalla_actual == 1:
         mostra_menu()

    # Mostra pantallade Crèdit
    elif pantalla_actual == 2:
        mostra_credits()


    elif pantalla_actual == 4:
        imprimir_pantalla_fons("assets/game_over.png")
        font = pygame.font.SysFont(None,100)
        text = "Player " + str(guanyador)+ "Wins!"
        img = font.render(text,True, WHITE)
        pantalla.blit(img,(180,400))

    elif pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge1, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vides_jugador2 =vides_jugador2-1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1
                pygame.init()
                ambient_music = pygame.mixer.Sound('assets/Sonidoexplosion.wav')
                ambient_music.play()



        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge2, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides_jugador1 = vides_jugador1 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1
                pygame.init()
                ambient_music = pygame.mixer.Sound('assets/Sonidoexplosion.wav')
                ambient_music.play()

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        #dibuixar vides juagador 1
        if vides_jugador1 >= 3:
            pantalla.blit(vides_image1,(615,550))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_image1, (650, 550))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_image1, (685, 550))
        # vides jugador 2
        if vides_jugador2 >= 3:
            pantalla.blit(vides_image2, (5, 5))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_image2, (32, 5))
        if vides_jugador2 >= 1:
            pantalla.blit(vides_image2, (60, 5))
        if vides_jugador1 <= 0 or vides_jugador2 <=0:
            ambient_music = pygame.mixer.Sound('assets/SonidoFondo.mp3')
            ambient_music.play()
            pantalla_actual = 4
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2
    pygame.display.update()
    clock.tick(fps)