import sys

input = sys.stdin.readline

N, M, row, col, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

# DIRECTIONS
EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def solution():
    global row, col

    #   1
    # 3 0 2
    #   4
    #   5

    # [윗면, 북, 동, 서, 남, 바닥]
    dice = [0, 0, 0, 0, 0, 0]

    for move in moves:
        # Calculate coordinates
        new_row = row + directions[move - 1][0]
        new_col = col + directions[move - 1][1]

        # Check if the dice is on the board
        if new_row < 0 or new_row > N - 1 or new_col < 0 or new_col > M - 1:
            continue
        
        # Roll the dice to update each sides
        if move == EAST:  # 동쪽
            new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif move == WEST:  # 서쪽
            new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif move == NORTH:  # 북쪽
            new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        elif move == SOUTH:  # 남쪽
            new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

        # Update position
        row, col = new_row, new_col

        # Check if the value of the updated coordinate is zero
        if board[new_row][new_col] == 0:
            board[new_row][new_col] = new_dice[5]
        else:
            new_dice[5] = board[new_row][new_col]
            board[new_row][new_col] = 0
        
        dice = new_dice[:]
        
        print(new_dice[0])


if __name__ == "__main__":
    solution()
