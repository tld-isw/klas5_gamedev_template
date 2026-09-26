"""Les 3: maak de objecten van de vijandengame."""
from game_core import Game, load_image
from actors import Player, Enemy, ChasingEnemy


class EnemyGame(Game):
    def __init__(self):
        super().__init__("Les 3 - Vijanden")
        self.player = self.add_object(Player(370, 225))
        # VERVANG DOOR PLAATJE: enemy_image = load_image("enemy.png", (32, 32))
        enemy_image = None
        self.add_object(Enemy(enemy_image, 90, 110))
        self.add_object(ChasingEnemy(enemy_image, 650, 310))

