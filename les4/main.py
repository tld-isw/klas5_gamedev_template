"""Les 4: plaats speler, munten en vijanden."""
from game_core import Game, load_image, start
from actors import Player, Enemy
from items import Coin


class CollisionGame(Game):
    def __init__(self):
        super().__init__("Les 4 - Botsingen")
        self.player = self.add_object(Player(85, 230))
        coin_image = load_image("gold_coin.png", (25, 25))
        enemy_image = load_image("ratman_voor.png", (38, 38))
        for x, y in [(200, 130), (450, 320)]:
            self.add_object(Coin(coin_image, x, y))
        for x, y in [(310, 220), (600, 260)]:
            self.add_object(Enemy(enemy_image, x, y))


if __name__ == "__main__":
    start(CollisionGame)
