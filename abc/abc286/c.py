n, a, b = map(int, input().split())
s = input()


def rotate_left(s, n):
    return s[n:] + s[:n]


ans = 10**9 * 5000
for i in range(n):
    cost = a * i
    rotate_s = rotate_left(s, i)

    i, j = 0, n - 1
    while i < j:
        if rotate_s[i] != rotate_s[j]:
            cost += b
        i += 1
        j -= 1

    ans = min(ans, cost)

print(ans)
