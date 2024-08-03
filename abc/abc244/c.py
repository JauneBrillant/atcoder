n = int(input())

used = set()
for _ in range(n * 2 + 1):
    for i in range(1, 2 * n + 2):
        if i not in used:
            print(i)
            used.add(i)
            break

    takahashi = int(input())
    if takahashi == 0:
        break
    else:
        used.add(takahashi)
