from collections import deque

h, w, n = map(int, input().split())
rc = [list(input()) for _ in range(h)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


start_i, start_j = next((i, j) for i in range(h) for j in range(w) if rc[i][j] == "S")
d = deque([(start_i, start_j)])

ans = 0
for target in range(1, n + 1):
    ok = False
    dist = [[-1] * w for _ in range(h)]
    dist[start_i][start_j] = 0

    while d:
        i, j = d.popleft()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and rc[ni][nj] != "X" and dist[ni][nj] == -1:
                d.append((ni, nj))
                dist[ni][nj] = dist[i][j] + 1
                if rc[ni][nj] == str(target):
                    ans += dist[ni][nj]
                    d.clear()
                    d.append((ni, nj))
                    start_i, start_j = ni, nj
                    ok = True
                    break
        if ok:
            break

print(ans)
