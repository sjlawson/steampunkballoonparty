# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="samuel"
__date__ ="$Mar 22, 2011 5:57:15 PM$"

import pygame, random

class Balloon(pygame.sprite.Sprite):
    """ Makes a balloon with random starting position """
    def __init__(self, color, screen):
        self.popNoise = pygame.mixer.Sound("pop.ogg")
        self.hits = 0
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,70))
        """Define the colour white as transparent"""
        self.image.set_colorkey((255,255,255))
        """Fill the bounding box with white, so it will be transparent"""
        self.image.fill((255,255,255))
        pygame.draw.ellipse(self.image, color, ((0,0), (50,60)), 0)
        pygame.draw.aaline(self.image, (240,240,240), (25, 60), (20,70), 1)
        pygame.draw.circle(self.image, color, (25,60), 2, 0 )
        pygame.draw.aaline(self.image, (240,240,240), (25, 60), (20,70), 1)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        
        self.x = self.rect.centerx
        self.y = self.rect.centery 
        startDir = random.randrange(0,8)
        
        self.dirList = (0, 45, 90, 135, 180, 225, 270, 315)      
        self.dir = self.dirList[startDir]
        self.speed = 2
        self.calcVector()
        
        #self.dx = 0
        #self.dy = 0
        
    def update(self, flyer):
        oldCenter = self.rect.center
        # self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.checkBounds()
        collisionResult = pygame.sprite.spritecollide(self, flyer, False)    
        if collisionResult:            
            #newDir = random.randrange(0,8)
            #self.dir = self.dirList[newDir]
            self.dx *= -1
            self.dy *= -1
            self.x += self.dx * 20
            self.y += self.dy * 20
            self.popNoise.play()
            #self.calcVector()
            if self.hits > 10:
                self.kill()
            else:
                self.hits += 1
            
        self.rect.center = oldCenter
        self.x += self.dx
        self.y += self.dy
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
    
    def calcVector(self):
        if self.dir == 0:
            self.dx = 1
            self.dy = 0
        elif self.dir == 45:
            self.dx = .7
            self.dy = -.7
        elif self.dir == 90:
            self.dx = 0
            self.dy = -1
        elif self.dir == 135:
            self.dx = -.7
            self.dy = -.7
        elif self.dir == 180:
            self.dx = -1
            self.dy = 0
        elif self.dir == 225:
            self.dx = -.7
            self.dy = .7
        elif self.dir == 270:
            self.dx = 0
            self.dy = 1
        elif self.dir == 315:
            self.dx = .7
            self.dy = .7
        else:
            print "something went wrong here"
        
        self.dx *= self.speed
        self.dy *= self.speed
        
    def checkBounds(self):
        screen = self.screen
        #if hit bottom
        if self.y > screen.get_height():
            self.dy *= -1
            #self.y = 0
        #if hit top
        if self.y < 0:
            self.dy *= -1
            #self.y = screen.get_height()
        #if hit right
        if self.x > screen.get_width():
            self.dx *= -1
            #self.x = 0
        #if hit left
        if self.x < 0:
            self.dx *= -1
            
            #self.x = screen.get_width()
    def balloonBounce(self):
        newDir = random.randrange(0,8)
        self.dir = self.dirList[newDir]

class Flyer(pygame.sprite.Sprite):
    """blue circle follows mouse"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        #self.image = pygame.image.load("flyer.png")
        self.image = pygame.image.load("flyer2.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-5,-5)
        

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
