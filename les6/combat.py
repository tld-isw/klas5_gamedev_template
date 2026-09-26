"""Les 6: Weapon maakt Bullet; Bullet handelt de treffer af."""
from game_core import GameObject, load_image
from enemy import Enemy


class Weapon:
    """Een wapen bewaart schade en kogelsnelheid en maakt een Bullet."""

    def __init__(self, damage=1, bullet_speed=440):
        self.damage = damage
        self.bullet_speed = bullet_speed

    def shoot(self, player):
        # VERVANG DOOR PLAATJE: bullet_image = load_image("bullet.png", (14, 10))
        bullet_image = None
        bullet = Bullet(bullet_image, player.x + player.width,
                        player.y + player.height / 2 - 5,
                        damage=self.damage, speed=self.bullet_speed)
        # Maken en toevoegen zijn twee aparte stappen; zoek ze in het werkboek.
        player.game.add_object(bullet)


class Bullet(GameObject):
    """Vliegt naar rechts en verdwijnt bij de rand of na een treffer."""

    def __init__(self, image, x, y, damage=1, speed=440):
        super().__init__(image, x, y, width=14, height=10, color=(255, 207, 87))
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

