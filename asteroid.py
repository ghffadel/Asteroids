from game_object import GameObject

from pygame.transform import rotozoom

from utils import *


class Asteroid(GameObject):
  def __init__(self, position, asteroid_callback, size=3):
    sprite = rotozoom(load_sprite('asteroid-%dx' % (2 ** (size + 3))), 0, 1)

    super().__init__(position, sprite, random_velocity(1, 3))

    self.asteroid_callback = asteroid_callback
    self.size = size

  def split(self):
    if self.size > 1:
      for i in range(2):
        asteroid = Asteroid(self.position, self.asteroid_callback, self.size - 1)
        self.asteroid_callback(asteroid)
