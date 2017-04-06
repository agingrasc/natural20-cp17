import pygame
from maploader import *

pygame.init()



def main():

    display_width = 800
    display_height = 600
    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Natural 20: Challenge Pixel 2017')
    clock = pygame.time.Clock()
    map = MapLoader()

    black = (0, 0, 0)
    white = (255, 255, 255)

    carImg = pygame.image.load('ressource/img/racecar.png')

    def car(x, y):
        game_display.blit(carImg, (x, y))

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)

            game_display.fill(white)
        car(x, y)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
