n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

for i in range(2 * n):
    t[(i + 1) % n] = min(t[(i + 1) % n], t[i % n] + s[i % n])

for ans in t:
    print(ans)
