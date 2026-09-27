"""Player: objecten van les 6."""
import pygame
from game_core import GameObject, load_image
from combat import Weapon


class Player(GameObject):
    """Beweegt, schiet en beheert zijn eigen health."""

    def __init__(self, x, y):
        super().__init__(load_image("mageheroman_voor.png", (36, 36)), x, y, width=36, height=36, color=(115, 211, 255))
        self.speed = 220
        self.max_health = 5
        self.health = 5
        self.weapon = Weapon()

    def update(self):
        x_direction = int(self.game.keys[pygame.K_d]) - int(self.game.keys[pygame.K_a])
        y_direction = int(self.game.keys[pygame.K_s]) - int(self.game.keys[pygame.K_w])

        self.move(x_direction, y_direction)
        self.keep_inside_world()
        if pygame.K_SPACE in self.game.just_pressed:
            self.weapon.shoot(self)

    def take_damage(self, amount):
        """Een ander object vraagt om schade; de speler wijzigt zijn health."""
        self.health = max(0, self.health - amount)

