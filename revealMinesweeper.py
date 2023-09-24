from collections import deque

MINE, HIDDEN, LOST = "M", "H", "X"


def revealMinesweeper(board, row, column):
    # 2D配列による条件分岐
    if board[row][column] == MINE:
        board[row][column] = LOST
        return board
    updateBoard(board, row, column)
    return board


def updateBoard(board, row, column):
    queue = deque()
    queue.append((row, column))
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]

    while queue:
        r, c = queue.popleft()
        totalMines = 0
        neighbors = []
        for dr, dc in directions:
            nr, nc = ((r + dr), (c + dc))
            if isOutOfBounds(nr, nc, board) or board[nr][nc].isdigit():
                continue
            if board[nr][nc] == MINE:
                totalMines += 1
            neighbors.append((nr, nc))
        board[r][c] = str(totalMines)
        if totalMines == 0:
            queue += neighbors


def isOutOfBounds(row, col, board):
    return row < 0 or col < 0 or row >= len(board) or col >= len(board[0])


test_board = [
    ["H", "M", "H", "H"],
    ["H", "H", "M", "H"],
    ["H", "M", "H", "H"],
    ["H", "H", "H", "H"],
]

# 初期状態のボードを表示
print("初期状態:")
for row in test_board:
    print(" ".join(row))

# (0, 0) の位置を選択して地雷を掘ります
updated_board = revealMinesweeper(test_board, 0, 0)

# 更新後のボードを表示
print("\n更新後:")
for row in updated_board:
    print(" ".join(row))
