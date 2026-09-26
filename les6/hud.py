"""Voorbeeld: teken de healthbar van Player boven op de game."""
import pygame


def draw_health_bar(screen, font, player):
    """Toon de huidige health als balk en als getal."""
    x, y, width, height = 16, 45, 180, 18
    pygame.draw.rect(screen, (65, 67, 86), (x, y, width, height), border_radius=5)
    fraction = player.health / player.max_health
    if fraction > 0:
        pygame.draw.rect(screen, (100, 214, 146),
                         (x, y, round(width * fraction), height), border_radius=5)
    label = font.render(f"Health: {player.health}/{player.max_health}",
                        True, (255, 255, 255))
    screen.blit(label, (x + 6, y - 1))
