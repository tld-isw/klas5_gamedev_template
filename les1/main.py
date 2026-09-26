"""Les 1: besturing lezen en uitbreiden. Start dit bestand."""
import pygame
from game_core import Game, GameObject, load_image, start


class Player(GameObject):
    """De speler controleert iedere frame welke pijltjestoets wordt gebruikt."""

    def __init__(self, x, y):
        # VERVANG DOOR PLAATJE: player_image = load_image("player.png", (36, 36))
        player_image = None
        super().__init__(player_image, x, y, width=36, height=36,
                         color=(115, 211, 255))
        self.speed = 200

    def update(self):
        # Startpunt van opdracht 1: alleen rechts werkt al.
        if self.game.keys[pygame.K_RIGHT]:
            self.move(1, 0)
        # Voeg hieronder zelf links, boven en beneden toe.
        # Later kun je hier ook een sprint met pygame.K_LSHIFT onderzoeken.
        self.keep_inside_world()


class Star(GameObject):
    """Een ster verhoogt de score en verdwijnt na aanraking."""

    def __init__(self, x, y):
        # VERVANG DOOR PLAATJE: star_image = load_image("star.png", (25, 25))
        star_image = None
        super().__init__(star_image, x, y, width=25, height=25,
                         color=(255, 207, 87), shape="circle")

    def update(self):
        if self.collides_with(self.game.player):
            self.game.score += 1
            self.remove()


class StarGame(Game):
    """De game maakt één speler en een paar sterren."""

    def __init__(self):
        super().__init__("Les 1 - Bewegen")
        self.player = self.add_object(Player(80, 230))
        for x, y in [(260, 240), (420, 115), (580, 330), (730, 230)]:
            self.add_object(Star(x, y))

