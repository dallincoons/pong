import arcade
from point import Point
from velocity import Velocity
import config
import random

RADIUS = 10

class Ball:
    def __init__(self):
        self.velocity = Velocity(random.uniform(-2, 2), random.uniform(-2, 2))
        self.center = Point(0, random.uniform(0, config.SCREEN_HEIGHT))

    def advance(self):
        self.center.x = self.center.x + self.velocity.dx
        self.center.y = self.center.y + self.velocity.dy

    def draw(self):
       arcade.draw_circle_filled(self.center.x, self.center.y, RADIUS, arcade.color.FUCHSIA)

    def bounce_horizontal(self):
        if (self.velocity.dx < 0):
            self.velocity.dx = 1
        elif (self.velocity.dx > 0):
            self.velocity.dx = -1

    def bounce_vertical(self):
        if (self.velocity.dy < 0):
            self.velocity.dy = 1
        elif (self.velocity.dy > 0):
            self.velocity.dy = -1

    def restart(self):
        self.center.x = 0
        self.center.y = random.uniform(0, config.SCREEN_HEIGHT)
        self.dx = random.uniform(1, 2)
        self.dy = random.uniform(1, 2)
