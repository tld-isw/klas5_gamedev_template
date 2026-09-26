"""Les 2: Player en Coin als game-objecten."""
import pygame
from game_core import GameObject, load_image


class Player(GameObject):
    """Speler met volledige besturing, zodat de aandacht naar instanties gaat."""

    def __init__(self, x, y):
        # VERVANG DOOR PLAATJE: player_image = load_image("player.png", (36, 36))
        player_image = None
        super().__init__(player_image, x, y, width=36, height=36,
                         color=(115, 211, 255))
        self.speed = 230

    def update(self):
        x_direction = int(self.game.keys[pygame.K_RIGHT]) - int(self.game.keys[pygame.K_LEFT])
        y_direction = int(self.game.keys[pygame.K_DOWN]) - int(self.game.keys[pygame.K_UP])
        self.move(x_direction, y_direction)
        self.keep_inside_world()


class Coin(GameObject):
    """Elke munt heeft een eigen positie en kan zichzelf verzamelen."""

    def __init__(self, image, x, y):
        super().__init__(image, x, y, width=25, height=25,
                         color=(255, 207, 87), shape="circle")
        # x en y komen van GameObject; iedere instantie bewaart eigen waarden.
        # Later in de les kun je hier self.value aan toevoegen.

    def update(self):
        if self.collides_with(self.game.player):
            self.collect()

    def collect(self):
        """Verhoog de score en verwijder alleen deze munt."""
        self.game.score += 10
        self.remove()

