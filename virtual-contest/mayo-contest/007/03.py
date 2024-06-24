n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

arr = []
for i, (a, b) in enumerate(ab):
    arr.append((a * (a + b), i + 1))

sorted_arr = sorted(arr, key=lambda x: (-x[0], x[1]))
res = [tup[1] for tup in sorted_arr]

for e in res:
    print(e)
