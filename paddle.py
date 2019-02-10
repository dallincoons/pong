from point import Point
from velocity import Velocity
import arcade
import config

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 30

class Paddle:

    def __init__(self):
        self.center = Point(390, 50)
        self.velocity = Velocity(0, 5)

    def draw(self):
        self.drawing = arcade.draw_rectangle_filled(self.center.x, self.center.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT, arcade.color.ELECTRIC_LIME)

    def move_up(self):
        if self.center.y < config.SCREEN_HEIGHT - (config.PADDLE_HEIGHT / 2):
            self.center.y = self.center.y + self.velocity.dy

    def move_down(self):
        if self.center.y > 0 + (config.PADDLE_HEIGHT / 2):
            self.center.y = self.center.y - self.velocity.dy
