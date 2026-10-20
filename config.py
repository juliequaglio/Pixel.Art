#Dimensoes da janela principal em pixels
SCREEN_WIDTH = 800 #largura da janela
SCREEN_HEIGHT = 600 #altura da janela

#Configuracoes do grid de pixel art
GRID_SIZE = 16 #nossa arte tera 16 x 16 pixels
CANVAS_SIZE = 480 #a area do desenho ocupara um quadrado de 480 x 480 pixels na tela
PIXEL_SIZE = CANVAS_SIZE // GRID_SIZE #480 // 16 = 30 pixels (// DIVISAO INTEIRA). Cada "pixel art" tera 30 x 30 pixels reais na tela

#Cores no formato RGB (Red, Green, Blue) - Valores de 0 a 255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (230, 230, 230)

#Lista de cores disponiveis na paleta
PALETTE_COLORS = [
    (0, 0, 0),     #preto
    (255, 255, 255), #branco
    (255, 0, 0),     #vermelho
    (0, 255, 0),    #verde
    (0, 0, 255),     #azul
    (255, 255, 0),   #amarelo
    (255, 128, 0),   #laranja
    (128, 0, 128),   #roxo
    (255, 192, 203), #rosa
    (139, 69, 19),   #marrom
    
]