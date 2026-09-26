"""Coin: objecten van les 6."""
from game_core import GameObject


class Coin(GameObject):
    """Een eerder patroon: botsen, score aanpassen en verwijderen."""

    def __init__(self, image, x, y):
        super().__init__(image, x, y, width=24, height=24,
                         color=(255, 207, 87), shape="circle")

    def update(self):
        if self.collides_with(self.game.player):
            self.game.score += 10
            self.remove()

