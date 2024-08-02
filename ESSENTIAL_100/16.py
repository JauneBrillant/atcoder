from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = b = 0
for i, perm in enumerate(permutations(range(1, n + 1))):
    if perm == p:
        a = i
    if perm == q:
        b = i

print(abs(a - b))
