"""
@Author: shubham shirke
@Date: 2022-06-03 14:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-03 14:15:30
@Title : Python stop watch program to find elapsed time between start and stop keyboard click.
"""
import random
#create 3x3 borad for tic-tac-toe game using 2D array
def create_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("---------")

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_computer_move(board):
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))
    return random.choice(available_moves)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    game_over = False
    while not game_over:
        create_board(board)

        if(current_player == "X"):
            row ,col = get_computer_move(board)
            print("Computer (Player 1) chooses row:", row, "column:", col)
        else:
            row  = int(input("Enter the row (0-2): "))
            col = int(input("Enter the colum (0-2): "))
        if board[row][col] != " ":
            print("Cell already occupied. Play again")
            continue
        board[row][col] = current_player

        if check_win(board ,current_player):
            create_board(board)
            if current_player == "X":
                print("Computer (Player 1) Wins")
            else:
                print("user (Player 2) wins!")
            game_over = True
        elif is_board_full(board):
            create_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"        

# main 
def main():
    print("Welcome to --Tic-Tac-Toe game--")
    play_game()

if __name__=="__main__":
    main()