from graphics.spriteSheet import SpriteSheet
import os.path
from graphics.animate import Animate
import pygame
import openal
import random

witch_sheet = SpriteSheet(os.path.join('res', "imgs", "witch.png"))
witch_sound = openal.oalOpen(os.path.join('res', 'sounds', 'witch.ogg'))
witch_sound1 = openal.oalOpen(os.path.join('res', 'sounds', 'witch1.ogg'))
witch_sound2= openal.oalOpen(os.path.join('res', 'sounds', 'witch2.ogg'))
witch_sound3 = openal.oalOpen(os.path.join('res', 'sounds', 'witch3.ogg'))
witch_sound4 = openal.oalOpen(os.path.join('res', 'sounds', 'witch4.ogg'))



class Entity:
    def __init__(self, x, y, width, height, sprite_sheet, source_sound):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = sprite_sheet.getSprites(scale=3, width=25, height=36, invisibleColor=0xff00ff, )
        self.animate = Animate(self.sprites)
        self.direction = 0
        self.current_sprite = self.sprites[0]
        self.source = openal.Source(source_sound)
        self.source.set_position((self.x, self.y, 0))
        self.time = 0
        self.direction = None

    def update(self):
        if self.time % 25 == 0:
            self.direction = random.randint(0, 3)
            print(self.direction)

        if self.direction == 0:
            self.current_sprite = self.animate.get_up()
            self.y -= 5
            if self.y < 75:
                self.y = 75
                self.time = -1

        elif self.direction == 1:
            self.current_sprite = self.animate.get_right()
            self.x += 5
            if self.x > (self.width - 200):
                self.x = self.width - 200
                self.time = -1

        elif self.direction == 2:
            self.current_sprite = self.animate.get_down()
            self.y += 5
            if self.y > (self.height - 200):
                self.y = self.height - 200
                self.time = -1

        elif self.direction == 3:
            self.current_sprite = self.animate.get_left()
            self.x -= 5
            if self.x < 75:
                self.x = 75
                self.time = -1

        self.source.set_position((self.x, self.y, 0))
        if self.source.get_state() != openal.AL_PLAYING:
            if random.randint(0,25) == 0:
                self.source.play()

        self.time += 1

    def draw(self, screen):
        screen.draw_image(self.current_sprite.image, self.x, self.y)
