from itertools import accumulate

n = int(input())
a = [0] + list(map(int, input().split())) + [0]
d = int(input())

acc_lr = list(accumulate(a, func=max))
acc_rl = list(accumulate(reversed(a), func=max))
acc_rl.reverse()

for _ in range(d):
    l, r = map(int, input().split())
    ans = max(acc_lr[l - 1], acc_rl[r + 1])
    print(ans)
