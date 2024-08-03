n, t = map(int, input().split())
a = list(map(int, input().split()))

sum = sum(a)
rest = t % sum

for i, ai in enumerate(a):
    if ai > rest:
        print(i + 1, rest)
        break
    rest -= ai
