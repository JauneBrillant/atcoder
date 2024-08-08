N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())
SIZE = 10 ** 5 + 1

# dp[n] = n段目に登ることが可能かどうか
dp = [False] * SIZE
dp[0] = True

for n in range(SIZE): 
    if not dp[n]:
        continue

    for a in A:
        if n + a < SIZE and n + a not in B:
            dp[n + a] = True

print("Yes" if dp[X] else "No")
