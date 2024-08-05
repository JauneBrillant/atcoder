from collections import deque

r, c = map(int, input().split())
start_i, start_j = map(int, input().split())
end_i, end_j = map(int, input().split())
grid = [list(input()) for _ in range(r)]

start_i, start_j = start_i - 1, start_j - 1
end_i, end_j = end_i - 1, end_j - 1

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dist = [[-1] * c for _ in range(r)]
dist[start_i][start_j] = 0
d = deque([(start_i, start_j)])

while d:
    i, j = d.popleft()
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == "." and dist[ni][nj] == -1:
            d.append((ni, nj))
            dist[ni][nj] = dist[i][j] + 1

print(dist[end_i][end_j])
