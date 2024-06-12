a, b = map(int, input().split())

ok = any(100 % i == 0 for i in range(a, b + 1))
print("Yes" if ok else "No")
