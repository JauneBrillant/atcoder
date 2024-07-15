n = int(input())
s = [input() for _ in range(n)]


def judge_bottom(i, j):
    cnt = 0
    for k in range(6):
        if s[i + k][j] == "#":
            cnt += 1
    return cnt >= 4


def judge_top(i, j):
    cnt = 0
    for k in range(6):
        if s[i - k][j] == "#":
            cnt += 1
    return cnt >= 4


def judge_right(i, j):
    cnt = 0
    for k in range(6):
        if s[i][j + k] == "#":
            cnt += 1
    return cnt >= 4


def judge_left(i, j):
    cnt = 0
    for k in range(6):
        if s[i][j - k] == "#":
            cnt += 1
    return cnt >= 4


def judge_cross_1(i, j):
    cnt = 0
    for k in range(6):
        if s[i + k][j + k] == "#":
            cnt += 1
    return cnt >= 4


def judge_cross_2(i, j):
    cnt = 0
    for k in range(6):
        if s[i - k][j + k] == "#":
            cnt += 1
    return cnt >= 4


def judge_cross_3(i, j):
    cnt = 0
    for k in range(6):
        if s[i + k][j - k] == "#":
            cnt += 1
    return cnt >= 4


def judge_cross_4(i, j):
    cnt = 0
    for k in range(6):
        if s[i - k][j - k] == "#":
            cnt += 1
    return cnt >= 4


def judge(i, j):
    if i + 5 < n and judge_bottom(i, j):
        return True
    if i - 5 >= 0 and judge_top(i, j):
        return True
    if j + 5 < n and judge_right(i, j):
        return True
    if j - 5 >= 0 and judge_left(i, j):
        return True
    if i + 5 < n and j + 5 < n and judge_cross_1(i, j):
        return True
    if i - 5 >= 0 and j + 5 < n and judge_cross_2(i, j):
        return True
    if i + 5 < n and j - 5 >= 0 and judge_cross_3(i, j):
        return True
    if i - 5 >= 0 and j - 5 >= 0 and judge_cross_4(i, j):
        return True

    return False


for i in range(n):
    for j in range(n):
        if s[i][j] == "#" and judge(i, j):
            print("Yes")
            exit()
print("No")
