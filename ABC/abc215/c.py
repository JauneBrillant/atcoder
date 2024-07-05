import itertools

s, k = input().split()
kk = int(k)

perm = sorted(set(itertools.permutations(s)))
print("".join(perm[kk - 1]))
