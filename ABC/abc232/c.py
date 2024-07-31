from itertools import permutations

n, m = map(int, input().split())
ga = [[False] * n for _ in range(n)]
gb = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ga[a][b] = True
    ga[b][a] = True
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    gb[a][b] = True
    gb[b][a] = True

for perm in permutations(range(n)):
    ok = True
    for i in range(n):
        for j in range(n):
            if ga[i][j] != gb[perm[i]][perm[j]]:
                ok = False
                break
#     if ok:
#         exit(print("Yes"))
# print("No")
