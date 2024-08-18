K = int(input())


def f(val, i):
    global seq
    seq.append(int("".join(map(str, val))))

    if i == 11:
        return

    last = val[-1]
    for j in [-1, 0, 1]:
        if last == 0 and j == -1 or last == 9 and j == 1:
            continue
        val.append(last + j)
        f(val, i + 1)
        val.pop()


seq = []
for i in range(1, 10):
    f([i], 1)

seq.sort()
print(seq[K - 1])
