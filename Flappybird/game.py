
import pygame, sys
from bird import Bird
from tube import Tube
def checkIsDead():
    if bird.birdRect.colliderect(tube.tubeRectTop):
        bird.isDead = True
        return True
    if bird.birdRect.colliderect(tube.tubeRectBott):
        bird.isDead = True
        return True
    if bird.birdY <= 0 or bird.birdY >= 600:
        bird.isDead = True
        return True
    else:
        bird.isDead = False
        return False
def gameOver():
    strGameOver = "Game Over"
    pygame.font.SysFont("Arial", 70)
    ft1 = font.render(strGameOver, 1,(222,45,2))
    screen.blit(ft1, (100, 100))
    screen.blit(scorerend, (400, 100))
    pygame.display.update()
def updateScreen():
    screen.blit(background, (0,0))
    screen.blit(tube.tubeImgTop, (tube.tubeX, -100))
    screen.blit(tube.tubeImgBott, (tube.tubeX, 500))
    if bird.jump == True:
        screen.blit(bird.birdImg[0], (bird.birdX, bird.birdY))
    else:
        screen.blit(bird.birdImg[1], (bird.birdX, bird.birdY))
    global scorerend
    scorerend = font.render("score: " + str(score), -1, (23,136,77))
    screen.blit(scorerend, (400, 100))
    tube.updateTube()
    bird.moveBird()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    screen = pygame.display.set_mode((800,600))
    colour = (255, 255, 255)

    clock = pygame.time.Clock()
    bird = Bird() 
    tube = Tube()
    global score
    score = 0
    
    while True:
        bird.jump = False
        clock.tick(60)
        #game refreshes 60 times per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                bird.jump = True
        screen.fill(colour)
        background = pygame.image.load("C:/Users/desto/OneDrive/Desktop/sky.png")
        if checkIsDead():
            gameOver()
        else: 
            updateScreen()
            if tube.tubeX == 240:
                score = score + 1