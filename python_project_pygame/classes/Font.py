from classes.Spriteheet import Spriteheet
import pygame


class Font(Spriteheet):
    def __init__(self, filePath, size):
        Spriteheet.__init__(self, filename=filePath)
        self.chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        self.charSprites = self.loadFont()

    def loadFont(self):
        font = {}
        row = 0
        charAt = 0

        for char in self.chars:
            if charAt == 16:
                charAt = 0
                row += 1
            font.update(
                {
                    char: self.image_at(
                        charAt,
                        row,
                        2,
                        colorkey=pygame.color.Color(0, 0, 0),
                        xTileSize=8,
                        yTileSize=8
                    )
                }
            )
            charAt += 1
        return font
