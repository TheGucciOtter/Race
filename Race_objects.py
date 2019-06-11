import pygame
from pygame.math import Vector2

VELOCITY_SCALE = 13

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.image = pygame.image.load('racecar.png')
        self.image = pygame.transform.scale(self.image, (53,42))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.velocity = 0
        self.direction = 0

    def update(self):
        self.position.x += self.velocity
        self.rect.x = self.position.x


    def accelerate(self):
        self.velocity += 1 / VELOCITY_SCALE

    def brake(self):
        self.velocity -= 1 / VELOCITY_SCALE

class Border(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        pygame.draw.rect(self.image, (0,0,0), [0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y
