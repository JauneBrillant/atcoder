from collections import deque

H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# -1: 沈んでいる
# 0: 海に隣接していない
# 1: 海に隣接している
lands_state = [
    [1 if i == 0 or i == H - 1 or j == 0 or j == W - 1 else 0 for j in range(W)]
    for i in range(H)
]
height_lands = sorted(
    [(A[i][j], i, j) for i in range(H) for j in range(W)], reverse=True
)


def cnt_sinking(i, j, y):
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    deq = deque([(i, j)])
    sinking_cnt = 1
    lands_state[i][j] = -1

    # deq := 現在の海面以下のセル、かつ海に隣接している
    while deq:
        i, j = deq.popleft()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                if lands_state[ni][nj] == 0:
                    lands_state[ni][nj] = 1
                if A[ni][nj] <= y and lands_state[ni][nj] != -1:
                    deq.append((ni, nj))
                    sinking_cnt += 1
                    lands_state[ni][nj] = -1

    return sinking_cnt


not_sinking_land = H * W
visited = set()
for y in range(1, Y + 1):
    while len(height_lands) > 0 and height_lands[-1][0] <= y:
        i, j = height_lands[-1][1], height_lands[-1][2]
        if lands_state[i][j] == 1:
            not_sinking_land -= cnt_sinking(i, j, y)
        height_lands.pop()
    print(not_sinking_land)
