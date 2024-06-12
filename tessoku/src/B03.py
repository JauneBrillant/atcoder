n = int(input())
a = list(map(int, input().split()))

ok = any(a[i] + a[j] + a[k] == 1000 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n))
print("Yes" if ok else "No")
