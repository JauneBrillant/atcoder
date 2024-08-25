N = int(input())
H = list(map(int, input().split()))

t = 0
for h in H:
    q, r = h // 5, h % 5
    t += 3 * q
    while r > 0:
        t += 1
        r -= 3 if t % 3 == 0 else 1

print(t)
