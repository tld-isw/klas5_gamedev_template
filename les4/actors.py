"""Les 4: Player en Enemy en hun botsing."""
import pygame
from game_core import GameObject, load_image


class Player(GameObject):
    def __init__(self, x, y):
        # VERVANG DOOR PLAATJE: image = load_image("player.png", (36, 36))
        super().__init__(None, x, y, width=36, height=36, color=(115, 211, 255))
        self.speed = 220
        self.health = 5
        # Health is hier nog bewust niet op het scherm zichtbaar.

    def update(self):
        x_direction = int(self.game.keys[pygame.K_RIGHT]) - int(self.game.keys[pygame.K_LEFT])
        y_direction = int(self.game.keys[pygame.K_DOWN]) - int(self.game.keys[pygame.K_UP])
        self.move(x_direction, y_direction)
        self.keep_inside_world()


class Enemy(GameObject):
    """Detecteert aanraking; gevolg wordt door de leerling gemaakt."""

    def __init__(self, image, x, y):
        super().__init__(image, x, y, width=35, height=35, color=(255, 137, 143))
        self.damage = 1  # Verdieping: verschillende vijanden krijgen eigen damage.

    def update(self):
        if self.collides_with(self.game.player):
            print("De speler is geraakt")

