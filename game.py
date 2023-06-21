import pygame,sys, random

pygame.init()

color=(0, 0, 0)

width = 800
height = 800

screen = pygame.display.set_mode((width, height))

#load images
invader = pygame.image.load("img/alien-de-juego.png")
invader2 = pygame.image.load("img/alien_yellow.png")
invader3 = pygame.image.load("img/alien_green.png")
spaceship = pygame.image.load("img/cohete.png")
ufo =  pygame.image.load("img/ovni.png")
shoot = pygame.image.load("img/misiles.png")
pygame.display.set_caption("stars")

#Definir posicion inicial del player
spaceshipX = 370
spaceshipY = 670
changeX = 0

#Definir condicion y posicion inicial del disparo
check = False
shootX = 370
shootY = 670

# Definir el tamaño de la matriz
filas = 2
columnas = 6

# Crear la matriz de imágenes
matrix_imagenes = [[invader] * columnas for _ in range(filas)]

# Definir las dimensiones de cada imagen
ancho_imagen = invader.get_width()
alto_imagen = invader.get_height()

ancho_ufo = ufo.get_width()
alto_ufo = ufo.get_height()


# Definir la posición inicial del ovni random
ufo_x = random.randint(0, width - ancho_ufo)
ufo_y = 15


# Definir el espacio entre las imágenes
espacio_entre_imagenes = 50
espacio_entre_imagenes_vertical = 240
espacio_entre_imagenesY = 120

# Calcular el tamaño total de la matriz en la pantalla
ancho_total = (ancho_imagen + espacio_entre_imagenes) * columnas - espacio_entre_imagenes
alto_total = (alto_imagen + espacio_entre_imagenes_vertical) * filas - espacio_entre_imagenes

# Calcular la posición inicial de la matriz en la pantalla
posicion_inicial_x = (width - ancho_total) // 2
posicion_inicial_y = (height - alto_total) // 2


# Definir el tamaño de la matriz 2
filas_amarillas = 1
columnas2 = 6

# Crear la matriz de imágenes
matrix_imagenes_amarilla = [[invader2] * columnas2 for _ in range(filas_amarillas)]

# Definir las dimensiones de cada imagen
ancho_imagen2 = invader2.get_width()
alto_imagen2 = invader2.get_height()

# Definir el espacio entre las imágenes
espacio_entre_imagenes2 = 50
espacio_entre_imagenes_vertical_amarillo = 360
espacio_entre_imagenesY2 = 200

# Calcular el tamaño total de la matriz en la pantalla
ancho_total2 = (ancho_imagen2 + espacio_entre_imagenes2) * columnas2 - espacio_entre_imagenes2
alto_total2 = (alto_imagen2 + espacio_entre_imagenes_vertical_amarillo) * filas_amarillas - espacio_entre_imagenes2

# Calcular la posición inicial de la matriz en la pantalla
posicion_inicial_x2 = (width - ancho_total2) // 2
posicion_inicial_y2 = (height - alto_total2) // 2


# Definir el tamaño de la matriz 3
filas_verdes = 1
columnas3 = 9

# Crear la matriz de imágenes
matrix_imagenes_verde = [[invader3] * columnas3 for _ in range(filas_verdes)]

# Definir las dimensiones de cada imagen
ancho_imagen3 = invader3.get_width()
alto_imagen3 = invader3.get_height()

# Definir el espacio entre las imágenes
espacio_entre_imagenes3 = 40
espacio_entre_imagenes_vertical_verde = -50
espacio_entre_imagenesY3 = 200

# Calcular el tamaño total de la matriz en la pantalla
ancho_total3 = (ancho_imagen3 + espacio_entre_imagenes3) * columnas3 - espacio_entre_imagenes3
alto_total3 = (alto_imagen3 + espacio_entre_imagenes_vertical_verde) * filas_verdes - espacio_entre_imagenes3

# Calcular la posición inicial de la matriz en la pantalla
posicion_inicial_x3 = (width - ancho_total3) // 2
posicion_inicial_y3 = (height - alto_total3) // 2


# Definir la velocidad y dirección del movimiento
velocidad_x = 1
direccion_x = 1

velocidad_x2 = 1
direccion_x2 = -1

velocidad_x3 = 1.4
direccion_x3 = 1

# Definir la velocidad del OVNI y dirección del movimiento en el eje y
velocidad_ufo_x = 2
direccion_ufo_x = random.choice([-1, 1])

# Definir el intervalo de tiempo para cambiar la dirección del movimiento
intervalo_tiempo = random.randint(1000, 5000)
tiempo_anterior = pygame.time.get_ticks()


while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
                
            if event.key == pygame.K_RIGHT:
                changeX = 1
                
            if event.key == pygame.K_SPACE:   
                if check is False:
                    check = True
                    shootX = spaceshipX + 12
                
        if event.type == pygame.KEYUP:
            changeX = 0
    
    spaceshipX+=changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736:
        spaceshipX=736
        
    if shootY <= 0:
        shootY = 670
        check = False
        
    if check is True:
        screen.blit(shoot, (shootX, shootY))
        shootY-= 5 
        
            
    # Actualizar la posición de la matriz en el eje x
    posicion_inicial_x += velocidad_x * direccion_x

    # Revertir la dirección si se alcanza el borde izquierdo o derecho
    if posicion_inicial_x <= 0 or posicion_inicial_x >= width - ancho_total:
        direccion_x *= -1    
        
    # Dibujar la matriz de imágenes en la pantalla
    for i in range(filas):
        for j in range(columnas):
            x = posicion_inicial_x + j * (ancho_imagen + espacio_entre_imagenes)
            y = posicion_inicial_y + i * (alto_imagen + espacio_entre_imagenesY)
            screen.blit(matrix_imagenes[i][j], (x, y))
            
    #matriz de la pantalla amarilla       
    # Actualizar la posición de la matriz en el eje x
    posicion_inicial_x2 += velocidad_x2 * direccion_x2

    # Revertir la dirección si se alcanza el borde izquierdo o derecho
    if posicion_inicial_x2 <= 0 or posicion_inicial_x2 >= width - ancho_total2:
        direccion_x2 *= -1    
        
    # Dibujar la matriz de imágenes en la pantalla
    for k in range(filas_amarillas):
        for l in range(columnas2):
            x2 = posicion_inicial_x2 + l * (ancho_imagen2 + espacio_entre_imagenes2)
            y2 = posicion_inicial_y2 + k * (alto_imagen2 + espacio_entre_imagenesY2)
            screen.blit(matrix_imagenes_amarilla[k][l], (x2, y2))          
            
            
    #matriz de la pantalla verde       
    # Actualizar la posición de la matriz en el eje x
    posicion_inicial_x3 += velocidad_x3 * direccion_x3

    # Revertir la dirección si se alcanza el borde izquierdo o derecho
    if posicion_inicial_x3 <= 0 or posicion_inicial_x3 >= width - ancho_total3:
        direccion_x3 *= -1    
        
    # Dibujar la matriz de imágenes en la pantalla
    for m in range(filas_verdes):
        for n in range(columnas3):
            x3 = posicion_inicial_x3 + n * (ancho_imagen3 + espacio_entre_imagenes3)
            y3 = posicion_inicial_y3 + m * (alto_imagen3 + espacio_entre_imagenesY3)
            screen.blit(matrix_imagenes_verde[m][n], (x3, y3))   
            
    # Actualizar la posición en el eje y del OVNI
    ufo_x += velocidad_ufo_x * direccion_ufo_x

    # Verificar si es necesario cambiar la dirección del movimiento
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_anterior >= intervalo_tiempo:
        direccion_ufo_x *= -1
        tiempo_anterior = tiempo_actual
        intervalo_tiempo = random.randint(1000, 5000)

    # Dibujar la imagen en la pantalla
    screen.blit(ufo, (ufo_x, ufo_y))
    screen.blit(spaceship, (spaceshipX, spaceshipY))

    pygame.display.update()
