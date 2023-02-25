import random
from math import floor

import pygame

screen = pygame.display.set_mode([900, 600], pygame.RESIZABLE)
LOWER_SPEED = 30
HIGHER_SPEED = 120
MAX_SIZE = 100
MIN_SIZE = 10

def draw_players(players):
    global screen
    for p in players:
        #p.size -= 1
        p.x -= p.speed[0]
        p.y -= p.speed[1]
        x = abs(p.x - abs(p.size / 2))
        y = abs(p.y - abs(p.size / 2))
        pygame.draw.ellipse(screen, [200,75,75], (x, y, abs(p.size), abs(p.size)))


def create_players(number_of_players):
    global screen
    players = []
    for i in range(0, number_of_players):
        size = random.randint(MIN_SIZE, MAX_SIZE)
        speed = [random.randint(LOWER_SPEED,HIGHER_SPEED)/size,random.randint(LOWER_SPEED,HIGHER_SPEED)/size]
        y_cord = random.randint(0 + size, floor(screen.get_rect().height - size / 2))
        x_cord = random.randint(0 + size, floor(screen.get_rect().width - size / 2))
        players.append(Player(y_cord, x_cord, size,speed))
    return players


class Player:
    def __init__(self, y_cord, x_cord, size,speed):
        self.alive = True
        self._y = y_cord
        self._x = x_cord
        self.score = 0
        self._size = size
        self.speed = speed

    @property
    def size(self):
        return self._size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @size.setter
    def size(self, size):
        if size < -MAX_SIZE:
            self._size = MAX_SIZE
        else:
            self._size = size

    @x.setter
    def x(self, x):
        if x <= -screen.get_rect().width + self._size*1.5:

            self._x = -x + self._size
        else:
            self._x = x

    @y.setter
    def y(self, y):
        if y <= -screen.get_rect().height + self._size*1.5:

            self._y = -y + self._size
        else:
            self._y = y
