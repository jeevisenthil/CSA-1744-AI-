import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for player in ['X', 'O']:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3)):
            return player
    return None

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O': return 1
    if winner == 'X': return -1
    if is_full(board): return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    temp = board[i][j]
                    board[i][j] = 'O'
                    best = max(best, minimax(board, False))
                    board[i][j] = temp
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    temp = board[i][j]
                    board[i][j] = 'X'
                    best = min(best, minimax(board, True))
                    board[i][j] = temp
        return best

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                temp = board[i][j]
                board[i][j] = 'O'
                move_val = minimax(board, False)
                board[i][j] = temp
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def play():
    board = [[str(3*i + j + 1) for j in range(3)] for i in range(3)]
    print_board(board)

    while True:
        move = input("Enter position (1-9): ")
        if move not in [str(n) for n in range(1, 10)]: continue
        r, c = divmod(int(move)-1, 3)
        if board[r][c] in ['X', 'O']:
            print("Occupied!")
            continue
        board[r][c] = 'X'

        winner = check_winner(board)
        if winner or is_full(board):
            print_board(board)
            print("Winner:", winner if winner else "Draw")
            break

        # AI move
        ai_r, ai_c = best_move(board)
        board[ai_r][ai_c] = 'O'

        winner = check_winner(board)
        print_board(board)
        if winner or is_full(board):
            print("Winner:", winner if winner else "Draw")
            break

play()
