"""Les 3: maak de objecten van de vijandengame."""
from game_core import Game, load_image, start
from actors import Player, Enemy, ChasingEnemy


class EnemyGame(Game):
    def __init__(self):
        super().__init__("Les 3 - Vijanden")
        self.player = self.add_object(Player(370, 225))
        enemy_image = load_image("ratman_voor.png", (38, 38))
        self.add_object(Enemy(enemy_image, 90, 110))
        self.add_object(ChasingEnemy(enemy_image, 650, 310))


if __name__ == "__main__":
    start(EnemyGame)
