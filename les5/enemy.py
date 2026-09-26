"""Enemy: objecten van les 5."""
import pygame
from game_core import GameObject, load_image


class Enemy(GameObject):
    """Heeft eigen health; raakt de speler en verdwijnt na een treffer."""

    def __init__(self, image, x, y, health=3):
        super().__init__(image, x, y, width=38, height=38, color=(255, 137, 143))
        self.health = health

    def update(self):
        if self.collides_with(self.game.player):
            self.game.player.take_damage(1)
            self.remove()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.remove()
            self.game.score += 1

    def draw(self, screen):
        super().draw(screen)
        # Klein vijandbalkje als extra voorbeeld van een eigenschap tekenen.
        pygame.draw.rect(screen, (70, 70, 85), (self.x, self.y - 9, 38, 5))
        pygame.draw.rect(screen, (255, 110, 130),
                         (self.x, self.y - 9, max(0, 38 * self.health / 3), 5))

