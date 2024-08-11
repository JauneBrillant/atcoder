import sys
sys.setrecursionlimit(10**4)

N, T, A = map(int, input().split())

rest = N - T - A
print("Yes" if T > A + rest or A > T + rest else "No")

