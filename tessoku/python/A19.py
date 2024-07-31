N, W = map(int, input().split())
ww = []
vv = []
for _ in range(N):
    w, v = map(int, input().split())
    ww.append(w)
    vv.append(v)

# 品物iまでの中で
# 重さjの時の
# 価値の最大値をdp[i][j]とする
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(W + 1):
        # 1: 品物 i - 1　の時点で合計が j であり、品物 i を選ばない
            
        # 2: 品物 i - 1　の時点で合計が i - wi であり、品物 i を選ぶ
