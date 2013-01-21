#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Samuel Lawson"
__date__ ="$20 December 2011 12:04:52 AM$"

import pygame, collisionObjects, random
pygame.init()

screen = pygame.display.set_mode((1360, 750))

def main():
    pygame.display.set_caption("Steampunk Balloon Party")

    background = pygame.Surface(screen.get_size())
    background.fill((100,100,255))
    screen.blit(background, (0,0))

    flyer = collisionObjects.Flyer()
    balloons = []
    for i in range(30):
        red = random.randrange(0, 255)
        green = random.randrange(0, 255)
        blue = random.randrange(0, 255)
        balloon = collisionObjects.Balloon((red,green,blue), screen)
        balloons.append(balloon)

    flyerSprite = pygame.sprite.Group(flyer)
    balloonGroup = pygame.sprite.Group(balloons)

#    popNoise = pygame.mixer.Sound("pop.ogg")

    #hide mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True
    startOver = False
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                if event.key == pygame.K_r:
                    keepGoing = False
                    startOver = True
                if event.key == pygame.K_b:
                    keepGoing = False
                    startOver = True
                    
        #if random.randrange(0,3) == 1:
        #    collisionResult = pygame.sprite.spritecollide(flyer, balloonGroup, True)
        #else:
#        collisionResult = pygame.sprite.spritecollide(flyer, balloonGroup, False)    
#        if collisionResult:
#            popNoise.play()

        balloonGroup.clear(screen, background)
        flyerSprite.clear(screen, background)

        balloonGroup.update(flyerSprite)
        flyerSprite.update()

        balloonGroup.draw(screen)
        flyerSprite.draw(screen)

        pygame.display.flip()

    if startOver:
        balloonGroup.clear(screen, background)
        flyerSprite.clear(screen, background)
        pygame.display.flip()
        main()

    pygame.mouse.set_visible(True)


if __name__ == "__main__":
    main()
