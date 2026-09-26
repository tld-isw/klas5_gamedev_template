"""Les 2: meerdere instanties van Coin maken en hun waarden vergelijken.

De twee munten en hun posities zijn precies de voorbeelden uit het werkboek.
De optionele eigenschap value staat er bewust nog niet in: die voeg je zelf toe."""
from game_core import Game, load_image, start
from objects import Player, Coin


class CoinGame(Game):
    """Maakt munt 1 en 2 afzonderlijk en voegt beide toe."""

    def __init__(self):
        super().__init__("Les 2 - Munten")
        self.player = self.add_object(Player(90, 230))
        # VERVANG DOOR PLAATJE: coin_image = load_image("coin.png", (25, 25))
        coin_image = None
        coin1 = Coin(
            coin_image,
            200,
            150
        )
        coin2 = Coin(
            coin_image,
            500,
            300
        )
        self.add_object(coin1)
        self.add_object(coin2)
        # Hier kun je later coin3 maken en toevoegen.


if __name__ == "__main__":
    start(CoinGame)
