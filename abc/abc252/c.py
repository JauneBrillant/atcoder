# 0 ~ 9 すべての数について、揃う時間の最小値を求める
# その中で最も小さいものが答え

# i = 揃えるかず
# j = リール番号
# t = 経過時間

n = int(input())
ss = [input() for _ in range(n)]

ans = 10**9
for i in range(10):
    selected = [False] * n
    cnt = 0
    t = 0
    while cnt < n:
        for j, s in enumerate(ss):
            if selected[j]:
                continue
            if s[t % 10] == str(i):
                selected[j] = True
                cnt += 1
                break
        t += 1
    ans = min(ans, t)

print(ans - 1)
