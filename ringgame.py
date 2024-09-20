import pygame as py
import random

# Initialize Pygame
py.init()

size = (500, 400)
screen = py.display.set_mode(size)

# Main loop
while True:
    for ev in py.event.get():
        if ev.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
            py.draw.circle(screen, col, pos, 20, 5)
            py.display.update()

        if ev.type == py.QUIT:
            py.quit()
            exit()
