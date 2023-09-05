import pygame

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

pygame.init()

screen_width=900
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SNAKEwithOMKAR")
pygame.display.update()

exit_game=False
exit_over=False
snake_x=45
snake_y=55
snake_size=10

while not exit_game:
        for event in pygame.event.get():
                print(event)
                if event.type==pygame.QUIT:
                        exit_game=True
                        
        gameWindow.fill(white)
        pygame.display.update()
        pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size])
pygame.quit()
quit()
