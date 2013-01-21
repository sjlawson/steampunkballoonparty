#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="samuel"
__date__ ="$Mar 23, 2011 12:04:52 AM$"

import pygame, collisionObjects
pygame.init()

screen = pygame.display.set_mode((1200, 900))

def main():
    pygame.display.set_caption("Using the collision library")

    background = pygame.Surface(screen.get_size())
    background.fill((100,100,255))
    screen.blit(background, (0,0))

    flyer = collisionObjects.Flyer()
    balloons = []
    for i in range(30):
        balloon = collisionObjects.Balloon((240,0,0), screen)
        balloons.append(balloon)

    flyerSprite = pygame.sprite.Group(flyer)
    balloonGroup = pygame.sprite.Group(balloons)

    popNoise = pygame.mixer.Sound("pop.ogg")

    #hide mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False

        collisionResult = pygame.sprite.spritecollide(flyer, balloonGroup, True)
        if collisionResult:
            popNoise.play()

        balloonGroup.clear(screen, background)
        flyerSprite.clear(screen, background)

        balloonGroup.update()
        flyerSprite.update()

        balloonGroup.draw(screen)
        flyerSprite.draw(screen)

        pygame.display.flip()


    pygame.mouse.set_visible(True)


if __name__ == "__main__":
    main()
