import pygame

pygame.init()

display = pygame.display
draw = pygame.draw
scrn_height , scrn_width  = 500 , 500
posX , posY  = 200 , 200
velocity = 10
game_screen = pygame.display.set_mode((scrn_height,scrn_width))
display.set_caption("Snake game")
class colors:

    red = (225,0,0)
    white = (225,225,225)
    black = (0,0,0)


game_end = False

while not game_end:

    pygame.time.delay(500)
    game_screen.fill(colors.white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
    pygame.draw.rect(game_screen,colors.black,[posX,posY,40,10])
    posX+=velocity
    pygame.display.update()
