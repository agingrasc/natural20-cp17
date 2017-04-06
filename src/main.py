import pygame

pygame.init()

def main():
    game_display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Natural 20: Challenge Pixel 2017')
    clock = pygame.time.Clock()

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
