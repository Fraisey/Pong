import pygame
import os

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

class Paddles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 20, 100))
        

class Pad1(Paddles):
    def __init__(self, x, y):
        super().__init__(x, y)
        
class Pad2(Paddles):
    def __init__(self, x, y):
        super().__init__(x, y)

class Ball:
    def __init__(self, x, y, xvel=3, yvel=3):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 20, 20))
        self.x += self.xvel
        self.y += self.yvel

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    vel = 7
    pad1 = Pad1(20, 275)
    pad2 = Pad2(760, 275)
    ball = Ball(390, 290)

    def redraw_window():
        WIN.fill((0, 0, 0))
        pad1.draw(WIN)
        pad2.draw(WIN)
        ball.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Paddle Border Checking
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and pad1.y > 0:
            pad1.y -= vel
        if keys[pygame.K_s] and pad1.y < 500:
            pad1.y += vel
        if keys[pygame.K_UP] and pad2.y > 0:
            pad2.y -= vel
        if keys[pygame.K_DOWN] and pad2.y < 500:
            pad2.y += vel
        
        # Ball Border Checking
        if ball.y >= 580 or ball.y <= 0:
            ball.yvel *= -1
        if ball.x < 20 or ball.x > 780:
            ball.x = 390
            ball.y = 290
        if ball.x >= pad2.x -20 and ball.y <= pad2.y + 80:
            ball.xvel *= -1
        if ball.x <= pad1.x + 20 and ball.y >= pad1.y - 80:
            ball.xvel *= -1

        
             
main()