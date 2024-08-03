import itertools

n = list(map(int, input()))


def to_number(lst):
    return int("".join(map(str, lst)))


ans = 0
for perm in itertools.permutations(n):
    for i in range(1, len(n)):
        left = to_number(list(perm)[:i])
        right = to_number(list(perm)[i:])
        ans = max(ans, left * right)

print(ans)
