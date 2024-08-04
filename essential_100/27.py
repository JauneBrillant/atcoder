m = int(input())
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(i, j, visited, cnt):
    global ans
    ans = max(ans, cnt)
    visited.add((i, j))

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited and grid[ni][nj]:
            dfs(ni, nj, visited, cnt + 1)
    visited.remove((i, j))


ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dfs(i, j, visited=set(), cnt=1)

print(ans)
