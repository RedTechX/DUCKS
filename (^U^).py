import pgzrun
import pygame

pygame.mouse.set_visible(False)

WIDTH = 900
HEIGHT = 700

ooooo = Actor('target_white')
oooo = Actor('target_colored')

ooooo.right = 0
ooooo.y = HEIGHT / 2

oooo.right = 0
oooo.bottom = HEIGHT

pOUT = Actor('crosshair_blue_large')
pIN = Actor('crosshair_blue_small')


def on_mouse_move(pos):
    pOUT.pos = pos
    pIN.pos = pos

def on_mouse_down(pos):
    if pIN.colliderect(ooooo):
        ooooo.right = -50
    
    if pIN.colliderect(oooo):
        oooo.x = -10

def update():
    #ooooo means 5 star difficulty
    ooooo.x += 8
    if ooooo.left > WIDTH:
        ooooo.right = -170
    
    #oooo means 4 star difficulty
    oooo.x += 6
    if oooo.left > WIDTH:
        oooo.right = -125


def draw():
    screen.clear()
    ooooo.draw()
    oooo.draw()
    
    pOUT.draw()
    pIN.draw()

pgzrun.go()