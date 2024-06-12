n = int(input())
a = list(map(int, input().split()))
q = int(input())

wins = [0] * (n + 1)
loses = [0] * (n + 1)

win_cnt = 0
lose_cnt = 0
for i in range(n):
    if a[i] == 1:
         win_cnt += 1
    else:
         lose_cnt += 1

    wins[i + 1] = win_cnt
    loses[i + 1] = lose_cnt

for _ in range(q):
    l, r = map(int, input().split())
    win = wins[r] - wins[l - 1]
    lose = loses[r] - loses[l - 1]

    if win == lose:
        print("draw")
    elif win > lose:
        print("win")
    else:
        print("lose")
