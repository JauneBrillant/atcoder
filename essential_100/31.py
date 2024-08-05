from collections import deque

w, h = map(int, input().split())
field = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
for i in range(h):
    field[i + 1][1 : w + 1] = map(int, input().split())

odd_dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]
even_dir = [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]

d = deque([(0, 0)])
visited = set()
ans = 0

while d:
    i, j = d.popleft()
    if i % 2 == 0:
        move = even_dir
    else:
        move = odd_dir

    for di, dj in move:
        ni, nj = i + di, j + dj
        if 0 <= ni < h + 2 and 0 <= nj < w + 2:
            if (ni, nj) in visited:
                continue

            if field[ni][nj] == 1:
                ans += 1
            else:
                d.append((ni, nj))
                visited.add((ni, nj))

print(ans)
