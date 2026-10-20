import pygame
from config import PALETTE_COLORS, BLACK, WHITE

class Palette:
    def __init__(self, x, y, box_size=40, margin=10):
        self.x = x
        self.y = y
        self.box_size = box_size
        self.margin = margin
        self.colors = PALETTE_COLORS
        self.selected_color = self.colors[0]

    def draw(self, surface):
        """Desenha os seletores de cor na tela em uma coluna vertical."""
        for i, color in enumerate (self.colors):
            box_x = self.x
            box_y = self.y + i * (self.box_size + self.margin)

            #Desenha o quadrado com a cor
            pygame.draw.rect(surface, color, (box_x, box_y, self.box_size, self.box_size))
            
            # Destaca a cor selecionada com uma borda branca/preta espessa
            if color == self.selected_color:
                pygame.draw.rect(surface, WHITE, (box_x - 3, box_y - 3, self.box_size + 6, self.box_size + 6), 3)
                pygame.draw.rect(surface, BLACK, (box_x - 1, box_y - 1, self.box_size + 2, self.box_size + 2), 1)
            else:
                pygame.draw.rect(surface, BLACK, (box_x, box_y, self.box_size, self.box_size), 1)

    def select_color(self, mouse_x, mouse_y):
        """Verifica se o usuário clicou em uma das cores da paleta."""
        for i, color in enumerate(self.colors):
            box_x = self.x
            box_y = self.y + i * (self.box_size + self.margin)

            if box_x <= mouse_x <= box_x + self.box_size and box_y <= mouse_y <= box_y + self.box_size:
                self.selected_color = color
                return color
        return None