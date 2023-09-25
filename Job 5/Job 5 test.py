import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 15
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
PLAYER_X = 'X'
PLAYER_O = 'O'
AI_PLAYER = 'O'
HUMAN_PLAYER = 'X'

# Initialize game variables
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = PLAYER_X
game_over = False
winner = None
ai_level = None  # To store AI difficulty level (easy, medium, hard)

# Create the game window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("TicTacToe1337")

# Fonts
font = pygame.font.Font(None, 48)
menu_font = pygame.font.Font(None, 36)

# Game Menu Options
MENU_OPTIONS = [
    {"text": "1. Easy", "level": "easy"},
    {"text": "2. Medium", "level": "medium"},
    {"text": "3. Hard", "level": "hard"},
]

# Functions
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(window, LINE_COLOR, (0, row * CELL_SIZE), (WINDOW_SIZE, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(window, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)

def draw_xo():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == PLAYER_X:
                x_center = col * CELL_SIZE + CELL_SIZE // 2
                y_center = row * CELL_SIZE + CELL_SIZE // 2
                x_offset = CELL_SIZE // 4
                pygame.draw.line(window, LINE_COLOR, (x_center - x_offset, y_center - x_offset),
                                 (x_center + x_offset, y_center + x_offset), LINE_WIDTH)
                pygame.draw.line(window, LINE_COLOR, (x_center - x_offset, y_center + x_offset),
                                 (x_center + x_offset, y_center - x_offset), LINE_WIDTH)
            elif board[row][col] == PLAYER_O:
                x_center = col * CELL_SIZE + CELL_SIZE // 2
                y_center = row * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 4
                pygame.draw.circle(window, LINE_COLOR, (x_center, y_center), radius, LINE_WIDTH)

def check_winner(player):
    # Check rows, columns, and diagonals for a winner
    for i in range(GRID_SIZE):
        if all(board[i][j] == player for j in range(GRID_SIZE)):
            return True
        if all(board[j][i] == player for j in range(GRID_SIZE)):
            return True
    if all(board[i][i] == player for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)):
        return True
    return False

def is_full():
    return all(board[i][j] != '' for i in range(GRID_SIZE) for j in range(GRID_SIZE))

def get_empty_cells():
    return [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] == '']

def is_valid_move(row, col):
    return 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and board[row][col] == ''

def ai_easy_move():
    empty_cells = get_empty_cells()
    return random.choice(empty_cells)

def ai_medium_move():
    # Check if AI can win
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if is_valid_move(row, col):
                board[row][col] = AI_PLAYER
                if check_winner(AI_PLAYER):
                    return row, col
                board[row][col] = ''

    # Check if player can win and block
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if is_valid_move(row, col):
                board[row][col] = HUMAN_PLAYER
                if check_winner(HUMAN_PLAYER):
                    return row, col
                board[row][col] = ''

    # Take a corner if available
    corners = [(0, 0), (0, GRID_SIZE - 1), (GRID_SIZE - 1, 0), (GRID_SIZE - 1, GRID_SIZE - 1)]
    available_corners = [corner for corner in corners if is_valid_move(corner[0], corner[1])]
    if available_corners:
        return random.choice(available_corners)

    # Take the center if available
    if is_valid_move(GRID_SIZE // 2, GRID_SIZE // 2):
        return GRID_SIZE // 2, GRID_SIZE // 2

    # Take any available edge
    edges = [(0, 1), (1, 0), (GRID_SIZE - 1, 1), (1, GRID_SIZE - 1)]
    available_edges = [edge for edge in edges if is_valid_move(edge[0], edge[1])]
    return random.choice(available_edges)

def ai_hard_move():
    def minimax(board, depth, is_maximizing):
        scores = {
            PLAYER_X: -1,
            PLAYER_O: 1,
            'tie': 0,
        }

        winner = check_winner(AI_PLAYER)
        if winner:
            return scores[winner]

        if is_maximizing:
            max_eval = -math.inf
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if is_valid_move(row, col):
                        board[row][col] = AI_PLAYER
                        eval = minimax(board, depth + 1, False)
                        board[row][col] = ''
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if is_valid_move(row, col):
                        board[row][col] = HUMAN_PLAYER
                        eval = minimax(board, depth + 1, True)
                        board[row][col] = ''
                        min_eval = min(min_eval, eval)
            return min_eval

    best_move = None
    best_eval = -math.inf
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if is_valid_move(row, col):
                board[row][col] = AI_PLAYER
                eval = minimax(board, 0, False)
                board[row][col] = ''
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def ai_move():
    if ai_level == "easy":
        return ai_easy_move()
    elif ai_level == "medium":
        return ai_medium_move()
    elif ai_level == "hard":
        return ai_hard_move()

def display_menu():
    menu_title = font.render("Select AI Difficulty Level:", True, LINE_COLOR)
    window.blit(menu_title, (50, 50))

    menu_y = 150
    for option in MENU_OPTIONS:
        text = menu_font.render(option["text"], True, LINE_COLOR)
        window.blit(text, (100, menu_y))
        menu_y += 50

    pygame.display.update()

def reset_game():
    global board, current_player, game_over, winner
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = PLAYER_X
    game_over = False
    winner = None

def main():
    global ai_level, game_over

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if is_valid_move(row, col):
                    board[row][col] = current_player
                    winner = check_winner(current_player)
                    if winner:
                        game_over = True
                    elif is_full():
                        game_over = True
                    else:
                        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                if event.key == pygame.K_m:
                    display_menu()
            if not game_over and ai_level and current_player == AI_PLAYER:
                ai_row, ai_col = ai_move()
                if is_valid_move(ai_row, ai_col):
                    board[ai_row][ai_col] = AI_PLAYER
                    winner = check_winner(AI_PLAYER)
                    if winner:
                        game_over = True
                    elif is_full():
                        game_over = True
                    else:
                        current_player = PLAYER_X

        window.fill(BG_COLOR)
        draw_grid()
        draw_xo()

        if winner:
            font = pygame.font.Font(None, 48)
            text = font.render(f'Player {winner} wins!', True, LINE_COLOR)
            window.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))
        elif game_over:
            font = pygame.font.Font(None, 48)
            text = font.render('It\'s a draw!', True, LINE_COLOR)
            window.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))

        pygame.display.update()

if __name__ == "__main__":
    display_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ai_level = "easy"
                    reset_game()
                elif event.key == pygame.K_2:
                    ai_level = "medium"
                    reset_game()
                elif event.key == pygame.K_3:
                    ai_level = "hard"
                    reset_game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
