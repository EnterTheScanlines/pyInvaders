import pygame,sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

#load images
spaceship = pygame.image.load("img/cohete.png")
pygame.display.set_caption("stars")

background = pygame.image.load("img/stars.jpg")
overlap = pygame.image.load("img/stars.jpg")

b_pos = 0
o_pos = -300
speed = 0.2

spaceshipX = 370
spaceshipY = 470
changeX = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -0.6
                
            if event.key == pygame.K_RIGHT:
                changeX = 0.6
                
        if event.type == pygame.KEYUP:
            changeX = 0

    
    spaceshipX+=changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736:
        spaceshipX=736
        
    if b_pos<=-height:
        b_pos=height
    if o_pos<=-height:
        o_pos=height
        
    b_pos += speed
    o_pos += speed
    screen.blit(background, (0, b_pos))
    screen.blit(overlap, (0, o_pos))
                
            
           
    screen.blit(spaceship, (spaceshipX, spaceshipY))
    pygame.display.update()
