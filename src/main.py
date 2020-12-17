import pygame
from graphics.screen import Canvas
import os.path
from player import Player
import entities.entity as e
from random import randint

pygame.init()

infoObject = pygame.display.Info()
Width, Height = infoObject.current_w, infoObject.current_h

path = os.path.join('res', "imgs", "witchBackGround.png")
print(path)
canvas = Canvas(Width, Height, 'OpenAl related stuff', path)
player = Player(Width // 2, Height // 2)

witch_sounds = [e.witch_sound, e.witch_sound1, e.witch_sound2, e.witch_sound3, e.witch_sound4]

witches = [
    e.Entity(randint(100, Width - 100), randint(100, Height - 100), Width, Height, e.witch_sheet, e.witch_sound)
]

running = True
clock = pygame.time.Clock()
time = pressed =  0
while running:
    time += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #
    if time % 3 == 0:
        keys = pygame.key.get_pressed()
        player.update(keys)
        for witch in witches:
            witch.update()
    if pressed == 0:
        if pygame.key.get_pressed()[pygame.K_n] and len(witches) < 200:
            witches.append(e.Entity(randint(100, Width - 100), randint(100, Height - 100), Width, Height, e.witch_sheet,
                                    witch_sounds[randint(0, len(witch_sounds) - 1)]))
            pressed = 20
    else:
        pressed -=1
    canvas.draw_back_ground()
    for witch in witches:
        witch.draw(canvas)
    player.draw(canvas)
    canvas.update()
