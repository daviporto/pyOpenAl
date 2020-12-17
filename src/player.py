from graphics.spriteSheet import SpriteSheet
import os.path
from graphics.animate import Animate
import pygame
import openal

player_sheet = SpriteSheet(os.path.join('res', "imgs", "player.png"), )


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprites = player_sheet.getSprites(scale=3,width=32, height=32, invisibleColor=0xff00ff, )
        self.animate = Animate(self.sprites)
        self.direction = 0
        self.current_sprite = self.sprites[0]
        self.listener = openal.Listener()
        self.listener.set_position((x, y, 2))

    def update(self, keys):
        self.current_sprite = self.sprites[0]

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.current_sprite = self.animate.get_left()
            self.x -=5
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.current_sprite = self.animate.get_right()
            self.x += 5

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.current_sprite = self.animate.get_down()
            self.y += 5
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.current_sprite = self.animate.get_up()
            self.y -= 5

        self.listener.set_position((self.x, self.y, 2))

    def draw(self, screen):
        if not self.direction:
            screen.draw_image(self.current_sprite.image, self.x, self.y)

