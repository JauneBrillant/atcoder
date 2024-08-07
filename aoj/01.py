from collections import deque

initial_board = tuple(tuple(map(int, input().split())) for _ in range(3))
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

i, j = next((i, j) for i in range(3) for j in range(3) if initial_board[i][j] == 0)
deq = deque([(initial_board, i, j, 0)])
seen = {initial_board}


ans = -1
while deq:
    board, i, j, step = deq.popleft()
    if board == ((1, 2, 3), (4, 5, 6), (7, 8, 0)):
        ans = step
        break

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            b = [list(row) for row in board]
            b[i][j], b[ni][nj] = b[ni][nj], b[i][j]
            t = tuple(tuple(r) for r in b)
            if t not in seen:
                seen.add(t)
                deq.append((t, ni, nj, step + 1))

print(ans)
