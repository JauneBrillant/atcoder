from itertools import permutations
from typing import Tuple

rc = [list(input()) for _ in range(8)]

# 初期配置をsetで持つ
pos: set[Tuple[int, int]] = set()
for i, row in enumerate(rc):
    for j, c in enumerate(row):
        if c == "Q":
            pos.add((i, j))


def print_grid(grid):
    for row in grid:
        print("".join(row))


def is_ok(grid):
    for i, j in pos:
        if grid[i][j] != "Q":
            return False
    return True


def is_eight_queen(grid):
    for i in range(8):
        for j in range(8):
            if grid[i][j] == "Q":
                base_i, base_j = i, j

                # 右上: i - 1, j + 1
                ii, jj = base_i, base_j
                while ii > 0 and jj < 7:
                    ii -= 1
                    jj += 1
                    if grid[ii][jj] == "Q":
                        return False

                # 右下: i + 1, j + 1
                ii, jj = base_i, base_j
                while ii < 7 and jj < 7:
                    ii += 1
                    jj += 1
                    if grid[ii][jj] == "Q":
                        return False

                # 左上: i - 1, j - 1
                ii, jj = base_i, base_j
                while ii > 0 and jj > 0:
                    ii -= 1
                    jj -= 1
                    if grid[ii][jj] == "Q":
                        return False

                # 左下: i + 1, j - 1
                ii, jj = base_i, base_j
                while ii < 7 and jj > 0:
                    ii += 1
                    jj -= 1
                    if grid[ii][jj] == "Q":
                        return False
    return True


# 各順列の「i: インデックス行目」、「j: インデックスに格納されている値列目」sr[i][j]が"Queen"だと仮定して判定
for perm in permutations(range(8)):
    # 盤面作成
    grid = [list("........") for _ in range(8)]
    for i, j in enumerate(perm):
        grid[i][j] = "Q"

    # 初期配置が違う場合
    if not is_ok(grid):
        continue

    # 8クイーン判定
    if is_eight_queen(grid):
        print_grid(grid)
        exit()

print("No Answer")
