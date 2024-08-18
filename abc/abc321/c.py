K = int(input())


def f(a):
    seq.append(int("".join(map(str, a))))

    last = a[-1]
    for j in range(last - 1, -1, -1):
        a.append(j)
        f(a)
        a.pop()


seq = []
for i in range(1, 10):
    f([i])

seq.sort()
print(seq[K - 1])
