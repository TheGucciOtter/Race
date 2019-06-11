import pygame as pg
import Race_objects
from pygame.math import Vector2

size = [1200, 700]
class RaceGame():
    def __init__(self):
        pg.init()
        pg.joystick.init()
        self.joystick = pg.joystick.Joystick(0)
        self.joystick.init()
        self.clock = pg.time.Clock()
        self.fps = 90
        self.done = False
        self.screen = pg.display.set_mode(size)
        self.player = Race_objects.Player(Vector2(600,350))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)
        self.border_right = Race_objects.Border(Vector2(1180,0),20,700)
        self.all_sprites.add(self.border_right)
        self.border_left = Race_objects.Border(Vector2(0,0),20,700)
        self.all_sprites.add(self.border_left)
        self.border_top = Race_objects.Border(Vector2(0,0),1200,20)
        self.all_sprites.add(self.border_top)
        self.border_bot = Race_objects.Border(Vector2(0,680),1200,20)
        self.all_sprites.add(self.border_bot)
        self.all_borders = pg.sprite.Group()
        self.all_borders.add(self.border_right)
        self.all_borders.add(self.border_left)
        self.all_borders.add(self.border_top)
        self.all_borders.add(self.border_bot)
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.yspeed += -10
                elif event.key == pg.K_s:
                    self.player.yspeed += 10
                elif event.key == pg.K_a:
                    self.player.xspeed += -10
                elif event.key == pg.K_d:
                    self.player.xspeed += 10

            elif event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.player.yspeed = 0
                elif event.key == pg.K_s:
                    self.player.yspeed = 0
                elif event.key == pg.K_a:
                    self.player.xspeed = 0
                elif event.key == pg.K_d:
                    self.player.xspeed = 0

        x = self.joystick.get_axis(0)
        y = self.joystick.get_axis(1)
        self.player.xspeed = x*10
        self.player.yspeed = y*10

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()
        if pg.sprite.spritecollide(self.player, self.all_borders, False):
            self.player.position = Vector2(600,350)

    def draw(self):
        self.screen.fill((255,255,255))
        self.all_sprites.draw(self.screen)

    def run(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)

game = RaceGame()
game.run()
