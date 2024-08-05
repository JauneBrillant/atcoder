n = int(input())
size = 2000 + 9
field = [[0] * (size) for _ in range(size)]
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    field[x][y] = 1

dir = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
visited = set()


def dfs(i, j):
    visited.add((i, j))

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < size
            and 0 <= nj < size
            and field[ni][nj] == 1
            and (ni, nj) not in visited
        ):
            dfs(ni, nj)


ans = 0
for i in range(size):
    for j in range(size):
        if field[i][j] == 1 and (i, j) not in visited:
            dfs(i, j)
            ans += 1

print(ans)
