from collections import deque

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
not_road = sum(1 for i in range(h) for j in range(w) if grid[i][j] == "#")

d = deque([(0, 0)])
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 1
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while d:
    i, j = d.popleft()

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and dist[ni][nj] == -1 and grid[ni][nj] == ".":
            d.append((ni, nj))
            dist[ni][nj] = dist[i][j] + 1

shortest_road = dist[h - 1][w - 1]
if shortest_road == -1:
    print(-1)
else:
    ans = h * w - shortest_road - not_road
    print(ans)
