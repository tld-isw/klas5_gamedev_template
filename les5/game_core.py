"""Kleine Pygame-basis voor de Gamedev-lessen.

Dit bestand regelt de game loop, posities, tekenen en botsingen. Leerlingen
veranderen voor de opdrachten vooral main.py. Iedere les heeft een eigen
kopie zodat een lesmap onafhankelijk van de andere mappen kan draaien.
"""

import asyncio
import math
from pathlib import Path

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60


def load_image(filename, size=None):
    """Laad een afbeelding uit de gedeelde map assets in de projectroot.

    Voorbeeld: load_image("mageheroman_voor.png", (36, 36)).
    Bij een ontbrekend bestand blijft de gekleurde vorm zichtbaar.
    """
    path = Path(__file__).resolve().parent.parent / "assets" / filename
    if not path.exists():
        return None
    image = pygame.image.load(str(path)).convert_alpha()
    return pygame.transform.smoothscale(image, size) if size else image


class GameObject:
    """Basisclass met positie, beweging, uiterlijk en eenvoudige botsing.

    x en y zijn de linkerbovenhoek. speed is in pixels per seconde;
    game.delta_time zorgt dat de beweging niet van de framerate afhangt.
    Een subclass vult update() aan voor zijn eigen gedrag.
    """

    def __init__(self, image, x, y, *, width=32, height=32,
                 color=(90, 110, 255), shape="rect"):
        self.image = image
        self.x = float(x)
        self.y = float(y)
        self.width = image.get_width() if image else width
        self.height = image.get_height() if image else height
        self.color = color
        self.shape = shape
        self.speed = 200
        self.game = None  # Wordt gezet door game.add_object(...).
        self.alive = True

    @property
    def rect(self):
        """De rechthoek waarmee we eenvoudige botsingen controleren."""
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)

    def update(self):
        """Wordt iedere frame aangeroepen; subclasses vullen dit in."""

    def draw(self, screen):
        """Teken een plaatje, of gebruik tijdelijk een herkenbare vorm."""
        if self.image is not None:
            screen.blit(self.image, (round(self.x), round(self.y)))
        elif self.shape == "circle":
            pygame.draw.circle(screen, self.color, self.rect.center,
                               min(self.width, self.height) // 2)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=5)

    def move(self, x_direction=0, y_direction=0):
        """Beweeg met gegeven richting (-1, 0, 1) en corrigeer diagonaal."""
        length = math.hypot(x_direction, y_direction)
        if length:
            scale = self.speed * self.game.delta_time / length
            self.x += x_direction * scale
            self.y += y_direction * scale

    def move_towards(self, other):
        """Beweeg naar het midden van een ander object."""
        dx = other.rect.centerx - self.rect.centerx
        dy = other.rect.centery - self.rect.centery
        self.move(dx, dy)

    def distance_to(self, other):
        """Afstand tussen de middelpunten van twee objecten."""
        return math.hypot(other.rect.centerx - self.rect.centerx,
                          other.rect.centery - self.rect.centery)

    def collides_with(self, other):
        """True wanneer de rechthoeken van twee objecten overlappen."""
        return self.alive and other.alive and self.rect.colliderect(other.rect)

    def at_world_edge(self):
        """True wanneer het object de grens van de wereld raakt."""
        return (self.x <= 0 or self.y <= 0 or
                self.x + self.width >= self.game.width or
                self.y + self.height >= self.game.height)

    def keep_inside_world(self):
        """Zet een object terug binnen de zichtbare spelwereld."""
        self.x = max(0, min(self.x, self.game.width - self.width))
        self.y = max(0, min(self.y, self.game.height - self.height))

    def remove(self):
        """Markeer voor verwijdering na deze update-ronde."""
        self.alive = False


class Game:
    """Beheert venster, input, objecten, game loop en score.

    De lesgame maakt een subclass en voegt in __init__ objecten toe.
    update() en draw_hud() kunnen per les een eigen invulling krijgen.
    """

    def __init__(self, title="Gamedev"):
        pygame.init()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.delta_time = 1 / FPS
        self.keys = pygame.key.get_pressed()
        self.just_pressed = set()
        self.objects = []
        self.player = None
        self.score = 0
        self.background_color = (23, 27, 51)
        self.background_image = load_image("field.png", (self.width, self.height))
        self.font = pygame.font.Font(None, 28)
        self.running = True

    def add_object(self, obj):
        """Bewaar het object in de game zodat het update en draw krijgt."""
        obj.game = self
        self.objects.append(obj)
        return obj

    def update(self):
        """Vervang in een lesgame wanneer je extra spelregels nodig hebt."""

    def draw_hud(self):
        """Teken informatie boven op de spelwereld; optioneel per les."""
        text = self.font.render(f"Score: {self.score}", True, (245, 245, 255))
        self.screen.blit(text, (16, 12))

    async def run(self, max_frames=None):
        """Voer input -> update -> draw uit, ook in de browser via Pygbag."""
        frames = 0
        while self.running:
            self.just_pressed.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.just_pressed.add(event.key)
            self.keys = pygame.key.get_pressed()
            self.delta_time = min(self.clock.tick(FPS) / 1000.0, 0.05)
            self.update()
            for obj in list(self.objects):
                if obj.alive:
                    obj.update()
            self.objects = [obj for obj in self.objects if obj.alive]
            if self.background_image is not None:
                self.screen.blit(self.background_image, (0, 0))
            else:
                self.screen.fill(self.background_color)
            for obj in self.objects:
                obj.draw(self.screen)
            self.draw_hud()
            pygame.display.flip()
            frames += 1
            if max_frames is not None and frames >= max_frames:
                break
            # Geef eventuele andere taken na elk frame kort de ruimte.
            await asyncio.sleep(0)
        pygame.quit()


def start(game_type):
    """Start Pygame op de desktop van Codespaces (poort 6080)."""
    asyncio.run(game_type().run())
