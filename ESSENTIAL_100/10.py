n = int(input())
a = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))


def solve(m):
    for bit in range(1 << n):
        sum = 0
        for i in range(n):
            if bit & 1 << i:
                sum += a[i]
        if sum == m:
            return True
    return False


for m in M:
    print("yes" if solve(m) else "no")
