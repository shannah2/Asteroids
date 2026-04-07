import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

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

    #Groups to cleanly update and draw multiple things at once.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Player is the name of the class, not an instance of it.
    #This must be done before any Player objects are created.
    #This should add all future instances of a Player to two different groups (updateable and drawable)
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    Score.containers = (drawable)

    #Instantiate a player
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    #Instantiate the score, so we can keep track. Potentially could be stored in Player.
    #May be better to do in its own class so we can try to draw it on screen cleaner.
    score = Score()

    #Instantiate the AsteroidField. This handles creating asteroids, so we don't need to instantiate those.
    asteroid_field = AsteroidField()

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
        
        #Update the everything in the updatable group.
        updatable.update(dt)
        
        #Check to see if any asteroids collide with the player.
        #If collision occurred, Game over!
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            #Looping over each shot to check if it has collided with the asteroid
            #Destroy bothe objects if it has.
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    points = asteroid.split()
                    #Manually calling update here since we only need to update if the player destroyed an asteroid.
                    #We don't need to update with every loop of the game.
                    score.update(points)
                    print(f"{score.score}")
                    shot.kill()
            

        #Filling the screen with solid black. This will be the background.
        screen.fill("black")
        #Loop over every member of drawable and .draw() them individually.
        for member in drawable:
            member.draw(screen)
        
        #Pause the game loop until 1/60th of a second has passed.
        #Also, storing the amount of time that has passed since the last time .tick() was called in dt (delta time).
        #Dividing by 1000 to convert from milliseconds to seconds.
        dt = (clock.tick(60))/1000
        
        #Refreshes the screen. This must be called last!
        pygame.display.flip()


if __name__ == "__main__":
    main()
