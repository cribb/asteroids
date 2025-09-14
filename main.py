import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clk = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    
    while True:
        # Make the game window's close ("x") button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black",rect=None,special_flags=0)
        pygame.display.flip()
        dt = clk.tick(60)/1000
        # print(f'fps= {1/dt}')

        
        
    
        

# Keep at end of file
if __name__ == "__main__":
    main()
 