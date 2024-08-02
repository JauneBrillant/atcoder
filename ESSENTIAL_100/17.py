from itertools import permutations

n = 8
rc = [list(input()) for _ in range(n)]
pos = {(i, j) for i in range(n) for j in range(n) if rc[i][j] == "Q"}


def print_rc():
    for row in rc:
        print("".join(row))


def clean_rc():
    for i in range(n):
        for j in range(n):
            rc[i][j] = "."


def is_ok():
    return all(rc[i][j] == "Q" for i, j in pos)


def is_eight_queen():
    dir = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    for i in range(n):
        for j in range(n):
            if rc[i][j] == "Q":
                for di, dj in dir:
                    ni, nj = i, j
                    while 0 <= ni + di < n and 0 <= nj + dj < n:
                        ni += di
                        nj += dj
                        if rc[ni][nj] == "Q":
                            return False
    return True


for perm in permutations(range(n)):
    clean_rc()
    for i, j in enumerate(perm):
        rc[i][j] = "Q"

    if is_ok() and is_eight_queen():
        print_rc()
        exit()

print("No Answer")
