import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as cores
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

# Configurações da tela
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo da Velha")

# Função para desenhar o degradê
def draw_gradient(screen, color1, color2):
    for i in range(height):
        color = [
            color1[j] + (color2[j] - color1[j]) * i // height
            for j in range(3)
        ]
        pygame.draw.line(screen, color, (0, i), (width, i))

# Função para desenhar o tabuleiro
def draw_board():
    draw_gradient(screen, PINK, WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (0, height // 3 * i), (width, height // 3 * i), 5)
        pygame.draw.line(screen, WHITE, (width // 3 * i, 0), (width // 3 * i, height), 5)

# Função para desenhar X e O
def draw_markers(board):
    for y in range(3):
        for x in range(3):
            if board[y][x] == "X":
                pygame.draw.line(screen, WHITE, (x * width // 3 + 50, y * height // 3 + 50), ((x + 1) * width // 3 - 50, (y + 1) * height // 3 - 50), 15)
                pygame.draw.line(screen, WHITE, ((x + 1) * width // 3 - 50, y * height // 3 + 50), (x * width // 3 + 50, (y + 1) * height // 3 - 50), 15)
            elif board[y][x] == "O":
                pygame.draw.circle(screen, WHITE, (x * width // 3 + width // 6, y * height // 3 + height // 6), width // 6 - 50, 15)

# Função para verificar vitória
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Função principal
def main():
    board = [[None, None, None], [None, None, None], [None, None, None]]
    player = "X"
    running = True
    winner = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                x, y = event.pos
                row, col = y // (height // 3), x // (width // 3)
                if board[row][col] is None:
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                    winner = check_winner(board)

        screen.fill(WHITE)
        draw_board()
        draw_markers(board)
        pygame.display.flip()

    if winner:
        print(f"Jogador {winner} venceu!")

if __name__ == "__main__":
    main()
