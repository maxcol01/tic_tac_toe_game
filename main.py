import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player
           for i in range(3)) or all(board[i][2 - i] == player
                                     for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells


def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (row, col) in get_empty_cells(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (row, col) in get_empty_cells(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '
            best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -math.inf
    best_move = None
    for (row, col) in get_empty_cells(board):
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


def player_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers.")
            continue
        try:
            row, col = int(move[0]), int(move[1])
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid move. Position out of bounds.")
            continue
        if board[row][col] != ' ':
            print("Invalid move. Cell already taken.")
            continue
        return (row, col)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    current_player = 'X'  # Player starts first

    while True:
        if current_player == 'X':
            row, col = player_move(board)
        else:
            row, col = ai_move(board)
            print(f"AI move: {row} {col}")

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
