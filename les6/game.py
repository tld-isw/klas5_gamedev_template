"""Les 6: maak de arena en teken de HUD."""
from game_core import Game, load_image
from player import Player
from enemy import Enemy, ChasingEnemy
from coin import Coin
from hud import draw_health_bar


class ArenaGame(Game):
    def __init__(self):
        super().__init__("Les 6 - Arena")
        self.player = self.add_object(Player(80, 235))
        # VERVANG DOOR PLAATJE: enemy_image = load_image("enemy.png", (38, 38))
        enemy_image = None
        self.add_object(Enemy(enemy_image, 525, 230))
        self.add_object(Enemy(enemy_image, 650, 315))
        self.add_object(ChasingEnemy(enemy_image, 690, 125))
        # VERVANG DOOR PLAATJE: coin_image = load_image("coin.png", (24, 24))
        coin_image = None
        self.add_object(Coin(coin_image, 280, 130))
        self.add_object(Coin(coin_image, 365, 360))

    def draw_hud(self):
        """De healthbar volgt steeds de werkelijke Player.health."""
        super().draw_hud()
        draw_health_bar(self.screen, self.font, self.player)

