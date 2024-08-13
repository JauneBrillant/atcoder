from itertools import permutations
from math import factorial

N, K = map(int, input().split())
S = input()

if len(set(S)) == N:
    print(factorial(N))
    exit()

ans = 0
for perm in set(permutations(S)):
    for i in range(N - K + 1):
        substr = perm[i : i + K]
        rev = substr[::-1]
        if substr == rev:
            break
    else:
        ans += 1

print(ans)
