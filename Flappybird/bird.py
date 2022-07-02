
import pygame
class Bird:
    def __init__(self):
        self.birdX = 250
        self.birdY = 300
        self.birdRect = pygame.Rect((self.birdX, self.birdY), (45,45))
        self.birdImg = [pygame.image.load("C:/Users/desto/OneDrive/Desktop/bird1.png"), 
                        pygame.image.load("C:/Users/desto/OneDrive/Desktop/bird2.png"),
                        pygame.image.load("C:/Users/desto/OneDrive/Desktop/bird3.png")]
        # if self.birdStat = 0 the bird is going straight. if it is 1, the bird is going up. if it is 2, the bird is going down.
        self.birdStat = 0
        self.jump = False
        self.jumpHeight = 50
        self.downSpeed = 2
        self.isDead = False
    def moveBird(self):
    # if self.jump = True, self.birdY = self.birdY + 10
        
        if self.jump == True:
            self.jumpHeight = 50
            self.birdY = self.birdY - self.jumpHeight
            self.jumpHeight = self.jumpHeight - 1
        else:
            self.downSpeed = 2
            self.birdY = self.birdY + self.downSpeed
            self.downSpeed = self.downSpeed + 0.02

        self.birdRect[1] = self.birdY