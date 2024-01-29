import pygame


class Block:
    def __init__(self, sprite, rect):
        self.sprite = sprite
        self.rect = rect

    def drawRect(self, screen):
        try:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), self.rect, 1)
        except Exception:
            pass
