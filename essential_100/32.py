from collections import deque


def solve():
    dist = [[0] * w for _ in range(h)]
    dist[0][0] = 1
    d = deque([(0, 0)])

    while d:
        i, j = d.popleft()

        # 右
        if j + 1 < w and row_rules[i][j] == 0 and dist[i][j + 1] == 0:
            dist[i][j + 1] = dist[i][j] + 1
            d.append((i, j + 1))

        # 左
        if j - 1 >= 0 and row_rules[i][j - 1] == 0 and dist[i][j - 1] == 0:
            dist[i][j - 1] = dist[i][j] + 1
            d.append((i, j - 1))

        # 上
        if i - 1 >= 0 and col_rules[i - 1][j] == 0 and dist[i - 1][j] == 0:
            dist[i - 1][j] = dist[i][j] + 1
            d.append((i - 1, j))

        # 下
        if i + 1 < h and col_rules[i][j] == 0 and dist[i + 1][j] == 0:
            dist[i + 1][j] = dist[i][j] + 1
            d.append((i + 1, j))

    print(dist[h - 1][w - 1])


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    row_rules = []
    col_rules = []
    for i in range(h):
        x = list(map(int, input().split()))
        row_rules.append(x)
        if i != h - 1:
            y = list(map(int, input().split()))
            col_rules.append(y)

    solve()
