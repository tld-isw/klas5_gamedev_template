"""Les 3: speler en vijandsoorten; bekijk de inheritance."""
import pygame
from game_core import GameObject, load_image


class Player(GameObject):
    def __init__(self, x, y):
        # VERVANG DOOR PLAATJE: image = load_image("player.png", (36, 36))
        super().__init__(None, x, y, width=36, height=36, color=(115, 211, 255))
        self.speed = 235

    def update(self):
        x_direction = int(self.game.keys[pygame.K_RIGHT]) - int(self.game.keys[pygame.K_LEFT])
        y_direction = int(self.game.keys[pygame.K_DOWN]) - int(self.game.keys[pygame.K_UP])
        self.move(x_direction, y_direction)
        self.keep_inside_world()


class Enemy(GameObject):
    """Een gewone vijand beweegt iedere frame in een vaste richting."""

    def __init__(self, image, x, y):
        super().__init__(image, x, y, width=32, height=32, color=(255, 137, 143))
        self.speed = 85
        self.health = 3

    def update(self):
        self.move(1, 0)
        # Begin opnieuw aan de linkerkant; zo blijft de vijand te onderzoeken.
        if self.x >= self.game.width:
            self.x = 0


class ChasingEnemy(Enemy):
    """Is een Enemy; gebruikt dezelfde kenmerken maar ander update-gedrag."""

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.color = (190, 124, 245)
        self.speed = 105

    def update(self):
        self.move_towards(self.game.player)

