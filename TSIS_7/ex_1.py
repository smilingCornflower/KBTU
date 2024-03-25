import pygame
import sys
from pygame.locals import *
from datetime import datetime
import math


pygame.init()


WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Clock")

base = pygame.image.load('mickeyclock.png')
base = pygame.transform.scale(base, WINDOW_SIZE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)


SECOND_LENGTH = 190
MINUTE_LENGTH = 150

def calculate_hand_end(angle, length):
    radian = math.radians(angle)
    return (
        CENTER[0] + math.sin(radian) * length,
        CENTER[1] - math.cos(radian) * length
    )


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(base, (0, 0))

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = (minute / 60) * 360 - 90
    second_angle = (second / 60) * 360 - 90


    minute_hand_end = calculate_hand_end(minute_angle, MINUTE_LENGTH)
    second_hand_end = calculate_hand_end(second_angle, SECOND_LENGTH)

    pygame.draw.line(screen, BLUE, CENTER, minute_hand_end, 3)
    pygame.draw.line(screen, RED, CENTER, second_hand_end, 2)

    pygame.display.flip()
    clock.tick(60)