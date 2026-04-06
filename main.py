import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    #Initialize pygame
    pygame.init()
    #Use display.set_mode function from pygame to get a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Create a clock object.
    clock = pygame.time.Clock()
    dt = 0

    #Instantiate a player
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    #Infinite while loop for the game loop
    while True:
        #Log stuff for boot.dev
        log_state()
        #For loop for processing events in the pygame event queue
        for event in pygame.event.get():
            #Checking to see if the game was quit out (X in the window was clicked). 
            #If it was, then actually quit the game.
            if event.type == pygame.QUIT:
                return
        #Filling the screen with solid black. This will be the background.
        screen.fill("black")
        #Draw Player
        player.draw(screen)
        #Pause the game loop until 1/60th of a second has passed.
        #Also, storing the amount of time that has passed since the last time .tick() was called in dt (delta time).
        #Dividing by 1000 to convert from milliseconds to seconds.
        dt = (clock.tick(60))/1000
        #Refreshes the screen. This must be called last!
        pygame.display.flip()


if __name__ == "__main__":
    main()
