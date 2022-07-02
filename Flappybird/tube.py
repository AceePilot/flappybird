import pygame
class Tube:
    def __init__(self):
        self.tubeImgTop = pygame.image.load(r"C:\Users\desto\Documents\Flappybird\picture\pipe2.png")
        self.tubeImgBott = pygame.image.load(r"C:\Users\desto\Documents\Flappybird\picture\pipe1.png")
        self.tubeX = 900
        self.tubeRectTop = pygame.Rect((self.tubeX, -100),(50, 400))
        self.tubeRectBott = pygame.Rect((self.tubeX, 500),(50, 400))

    
    def updateTube(self):
        if self.tubeX <= 0:
            self.tubeX = 900
        else:
            self.tubeX = self.tubeX - 3
        self.tubeRectTop[0] = self.tubeX
        self.tubeRectBott[0] = self.tubeX
