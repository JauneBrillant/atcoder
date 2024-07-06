x = input()
n = int(input())
ss = [input() for _ in range(n)]


def substitute(s, hashmap):
    return "".join(hashmap[c] for c in s)


hashmap = {c: chr(ord("a") + i) for i, c in enumerate(x)}
for res in sorted(ss, key=lambda s: substitute(s, hashmap)):
    print(res)
