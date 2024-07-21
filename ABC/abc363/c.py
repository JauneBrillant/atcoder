import itertools
import math

n, k = map(int, input().split())
s = list(input())

if len(set(s)) == n:
    print(math.factorial(n))
    exit()


def is_palindrome(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True


permutations = set(itertools.permutations(s))
ans = 0
for perm in permutations:
    ok = True
    for i in range(n - k + 1):
        if is_palindrome(perm[i : i + k]):
            ok = False
            break
    if ok:
        ans += 1


print(ans)
