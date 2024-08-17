A, B, C = map(int, input().split())

if B < C:
    print("No" if B < A < C else "Yes")
else:
    print("Yes" if C < A < B else "No")
