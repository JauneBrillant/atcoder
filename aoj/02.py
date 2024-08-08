from collections import deque

H, W = map(int, input().split())
grid = tuple(tuple(map(int, input().split())) for _ in range(H))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
correct = tuple(tuple((i * W + j) % (H * W) + 1 for j in range(W)) for i in range(H))
correct = correct[:-1] + (correct[-1][:-1] + (0,),)

i, j = next((i, j) for i in range(H) for j in range(W) if grid[i][j] == 0)

deq = deque([(grid, i, j, 0)])
seen = { grid }

ans = -1
while deq:
    state, i, j, depth = deq.popleft()
    if state == correct: 
        ans = depth
        break
        
    if depth = 23:
        ans = 23
        break

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            lst = list(list(row) for row in state)
            lst[i][j], lst[ni][nj] = lst[ni][nj], lst[i][j]
            t = tuple(tuple(row) for row in lst)
            if t not in seen:
                seen.add(t)
                deq.append((t, ni, nj, depth + 1))

print(ans)


