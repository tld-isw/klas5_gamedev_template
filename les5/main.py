"""Les 5: maak de arena en teken de HUD."""
from game_core import Game, load_image, start
from player import Player
from enemy import Enemy
from hud import draw_health_bar


class ShooterGame(Game):
    def __init__(self):
        super().__init__("Les 5 - Wapen en health")
        self.background_image = load_image("grotto.png", (self.width, self.height))
        self.player = self.add_object(Player(80, 235))
        enemy_image = load_image("ratman_voor.png", (38, 38))
        self.add_object(Enemy(enemy_image, 525, 230))
        self.add_object(Enemy(enemy_image, 650, 315))
        self.add_object(Enemy(enemy_image, 690, 125))

    def draw_hud(self):
        """De healthbar volgt steeds de werkelijke Player.health."""
        super().draw_hud()
        draw_health_bar(self.screen, self.font, self.player)


if __name__ == "__main__":
    start(ShooterGame)
