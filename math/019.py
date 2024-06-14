def nc2(n):
    return n * (n - 1) // 2


n = int(input())
a = list(map(int, input().split()))

print(nc2(a.count(1)) + nc2(a.count(2)) + nc2(a.count(3)))
