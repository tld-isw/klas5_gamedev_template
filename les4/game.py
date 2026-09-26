"""Les 4: plaats speler, munten en vijanden."""
from game_core import Game, load_image
from actors import Player, Enemy
from items import Coin


class CollisionGame(Game):
    def __init__(self):
        super().__init__("Les 4 - Botsingen")
        self.player = self.add_object(Player(85, 230))
        # VERVANG DOOR PLAATJE: coin_image = load_image("coin.png", (24, 24))
        coin_image = None
        # VERVANG DOOR PLAATJE: enemy_image = load_image("enemy.png", (35, 35))
        enemy_image = None
        for x, y in [(200, 130), (450, 320)]:
            self.add_object(Coin(coin_image, x, y))
        for x, y in [(310, 220), (600, 260)]:
            self.add_object(Enemy(enemy_image, x, y))

