import sys
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHT_GRAY, DARK_GRAY
from grid import Grid
from palette import Palette

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Art Studio - Didático")
        self.clock = pygame.time.Clock()
        self.running = True

        #Instancia as classes componentes
        self.grid = Grid(x_offset=20, y_offset=20)
        self.palette = Palette(x=530, y=20)
        self.font = pygame.font.SysFont("Arial", 16)

    def run(self):
        """Loopprincipal da aplicação."""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60) #mantem o programa rodando a 60 FPS

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """trata cliques de mouse e pressionamento de teclas."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                # Pressionar 'C' para limpar a tela
                if event.key == pygame.K_c:
                    self.grid.clear()

        #Clique e arraste do mouse para desenhar continuamente
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Botão esquerdo do mouse pressionado
            pos = pygame.mouse.get_pos()
            # Tenta selecionar uma cor na paleta
            selected = self.palette.select_color(pos[0], pos[1])
            # Se não clicou na paleta, pinta no canvas
            if not selected:
                self.grid.set_pixel(pos[0], pos[1], self.palette.selected_color)

    def draw(self):
        """Renderiza todos os elementos na janela."""
        self.screen.fill(LIGHT_GRAY)

        # Desenha os componentes
        self.grid.draw(self.screen)
        self.palette.draw(self.screen)

        # Instruções na tela
        instructions = "Botão Esquerdo: Pintar | Tecla C: Limpar Canvas"
        text_surface = self.font.render(instructions, True, DARK_GRAY)
        self.screen.blit(text_surface, (20, 520))

        pygame.display.flip()

if __name__ == "__main__":
    app = App()
    app.run()