n = int(input())
p = list(map(int, input().split()))

q = [0] * n
for i, e in enumerate(p):
    q[e - 1] = i + 1

for e in q:
    print(e)
