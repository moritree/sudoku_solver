import sys
import math


done = False


# Prints the current board to the console
def print_board(board):
    print("-------------------------")
    for i in range(9):
        if i in (3, 6):
            print("|-----------------------|")
        print("| ", end="")
        for j in range(9):
            if j in (3, 6):
                print("| ", end="")
            if str(board[i][j]) == '0':
                print("-" + " ", end="")
            else:
                print(str(board[i][j]) + " ", end="")
        print("|")
    print("-------------------------")


# Checks all possibilities for the square located at x y
def possibilities(board, y, x):
    options = []

    for i in range(1, 10):
        flag = False

        # Check row
        for j in range(9):
            if board[y][j] == i:
                flag = True

        # Check column
        for j in range(9):
            if board[j][x] == i:
                flag = True

        # Check 3x3 squares
        for j in range(int(math.floor(y / 3) * 3), int(math.floor(y / 3) * 3) + 3):
            for k in range(int(math.floor(x / 3) * 3), int(math.floor(x / 3) * 3) + 3):
                if board[j][k] == i:
                    flag = True

        if not flag:
            options.append(i)

    return options


# Recursive algorithm to solve the puzzle
def recursive_solve(board, solved):
    if not is_full(board, solved):
        y = 0
        x = 0

        # Find first free spot
        flag = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0 and not flag:
                    y = i
                    x = j
                    flag = True

        if not is_full(board, solved):
            # Recursion into each possibility
            for item in possibilities(board, y, x):
                board[y][x] = item
                recursive_solve(board, solved)
            # Backtrack
            if not is_full(board, solved):
                board[y][x] = 0
    else:
        return


# Checks whether the board has been filled or not
# If there are any zeroes present, the board is not full
def is_full(board, solved):
    flag = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                flag = False
    if flag and solved[0][0] == 0:
        for i in range(9):
            for j in range(9):
                solved[i][j] = board[i][j]
    return flag


def main():
    if len(sys.argv) < 2:
        print("USAGE: " + sys.argv[0] + " FILENAME")

    board = [[0] * 9 for i in range(9)]
    solved = [[0] * 9 for i in range(9)]

    # Write puzzle file to array
    try:
        with open(sys.argv[1], 'r') as f:
            for x in range(9):
                for y in range(9):
                    board[x][y] = int(f.read(1))
                    f.seek(f.tell() + 1)
    except FileNotFoundError:
        print("File not found.")
        return 1

    print("Puzzle: ")
    print_board(board)
    recursive_solve(board, solved)
    print("\nSolved!")
    print_board(solved)


if __name__ == '__main__':
    main()
