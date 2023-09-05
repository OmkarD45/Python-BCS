import pygame
x=pygame.init()
#creating window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

#game specific variables
exit_game=False
game_over=False


#creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                exit_game=True


        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("you have pressed right arrow key")
                
pygame.quit()
quit()
