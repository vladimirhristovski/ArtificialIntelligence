import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def minesweeper_update_2(matrix, n):
    for m in range(n):
        for j in range(n):
            if matrix[m][j] != "#":
                matrix[m][j] = 0
    for m in range(n):
        for j in range(n):
            if matrix[m][j] == "#":
                if j - 1 >= 0 and matrix[m][j - 1] != "#":  # left
                    matrix[m][j - 1] += 1
                if j + 1 <= n - 1 and matrix[m][j + 1] != "#":  # right
                    matrix[m][j + 1] += 1
                if m - 1 >= 0 and matrix[m - 1][j] != "#":  # up
                    matrix[m - 1][j] += 1
                if m + 1 <= n - 1 and matrix[m + 1][j] != "#":  # down
                    matrix[m + 1][j] += 1
                if j - 1 >= 0 and m - 1 >= 0 and matrix[m - 1][j - 1] != "#":  # up-left
                    matrix[m - 1][j - 1] += 1
                if j + 1 <= n - 1 and m - 1 >= 0 and matrix[m - 1][j + 1] != "#":  # up-right
                    matrix[m - 1][j + 1] += 1
                if m + 1 <= n - 1 and j - 1 >= 0 and matrix[m + 1][j - 1] != "#":  # down-left
                    matrix[m + 1][j - 1] += 1
                if m + 1 <= n - 1 and j + 1 <= n - 1 and matrix[m + 1][j + 1] != "#":  # down_right
                    matrix[m + 1][j + 1] += 1
    string = ""
    for m in range(n):
        if m != 0:
            string += "\n"
        for j in range(n):
            if j == n:
                string += str(matrix[m][j])
            else:
                string += str(matrix[m][j]) + "   "
    print(string)


def update_mines(a, j, matrix):
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    mines_around = 0
    for x, y in directions:
        ni, nj = a + x, j + y
        if ni in range(len(matrix)) and nj in range(len(matrix)) and matrix[ni][nj] == "#":
            mines_around += 1

    return mines_around


def minesweeper_update(matrix):
    return [[update_mines(a, j, matrix) if matrix[a][j] != "#" else "#" for j in range(len(matrix))] for a in
            range(len(matrix))]


if __name__ == "__main__":
    input_size = input()
    minesweeper = []
    for i in range(int(input_size)):
        minesweeper.append(input().split())
    # minesweeper_update_2(minesweeper, int(input_size))
    updated_minesweeper = minesweeper_update(minesweeper)

    for row in updated_minesweeper:
        print("   ".join(str(col) for col in row))
