import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clk = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable) # added here as static class variables to Player
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop    
    while True:
        # Make the game window's close ("x") button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black",rect=None,special_flags=0)
        
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        
        pygame.display.flip()
        dt = clk.tick(60)/1000
        # print(f'fps= {1/dt}')

        
        
    
        

# Keep at end of file
if __name__ == "__main__":
    main()
 


# - In the initialization code in main (before the game loop starts), create a new 
#   pygame.sprite.Group which will contain all of the asteroids.
# - Like we did with the Player class, set the static containers field of the Asteroid 
#   class to the new asteroids group, as well as the updatable and drawable groups.