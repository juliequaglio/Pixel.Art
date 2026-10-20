import pygame
from config import GRID_SIZE, PIXEL_SIZE, WHITE, GRAY

class Grid:
    def __init__(self, x_offset=10, y_offset=10):
        self.x_offset = x_offset
        self.y_offset = y_offset
        #Matriz GRID_SIZE x  GRID_SIZE preenchida com a cor branca
        self.matriz = [[WHITE for _ in range(GRID_SIZE) for _ in range(GRID_SIZE)]]
    def draw(self, surface):
        """Desenha cada quadrado do grid e as linhas divisorias"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = self.x_offset + col * PIXEL_SIZE
                y = self.y_offset + row * PIXEL_SIZE
                color = self.matriz[row][col]

                #Desenha o pixel colorido
                pygame.draw.rect(surface, color, (x, y, PIXEL_SIZE, PIXEL_SIZE))
                #Desenha a borda fina (linha da grade)
                pygame.draw.rect.(surface, GRAY, (x, y, PIXEL_SIZE, PIXEL_SIZE), 1)

    def set_pixel(self, mouse_x, mouse_y, color):
        """Converte as coordenadas do mouse para posicoes da matriz e altera a cor"""
        rel_x = mouse_x - self.x_offset
        real_y = mouse_y - self.y_offset

        #verfica se o clique foi dentro da area do canvas
        if 0 <= rel_x < GRID_SIZE * PIXEL_SIZE and 0 <= rel_y < GRID_SIZE * PIXEL_SIZE:
            col = rel_x // PIXEL_SIZE
            row = rel_y // PIXEL_SIZE
            self.matrix[row][col] = color

    def clear(self):
        """Limpa a tela redefinindo todos os pixels para a cor branca."""
        self.matrix = [[WHITE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                      