"""Les 5: Weapon maakt Fireball; Fireball handelt de treffer af."""
from game_core import GameObject, load_image
from enemy import Enemy


class Weapon:
    """Een wapen bewaart schade en snelheid van vuurballen en maakt een Fireball."""

    def __init__(self, damage=1, fireball_speed=440):
        self.damage = damage
        self.fireball_speed = fireball_speed

    def shoot(self, player):
        fireball_image = load_image("blue_fire_small.png", (14, 14))
        fireball = Fireball(fireball_image, player.x + player.width,
                            player.y + player.height / 2 - 7,
                            damage=self.damage, speed=self.fireball_speed)
        # Maken en toevoegen zijn twee aparte stappen; zoek ze in het werkboek.
        player.game.add_object(fireball)


class Fireball(GameObject):
    """Vuurbol vliegt naar rechts en verdwijnt bij de rand of een treffer."""

    def __init__(self, image, x, y, damage=1, speed=440):
        super().__init__(image, x, y, width=14, height=14, color=(80, 175, 255))
        self.damage = damage
        self.speed = speed

    def update(self):
        self.move(1, 0)
        if self.at_world_edge():
            self.remove()
            return
        for enemy in self.game.objects:
            if isinstance(enemy, Enemy) and self.collides_with(enemy):
                enemy.take_damage(self.damage)
                self.remove()
                break
