import arcade
from pong import Pong

def main():
    # Creates the game and starts it going
    window = Pong(Pong.SCREEN_WIDTH, Pong.SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
