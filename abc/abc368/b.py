N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
while A[1] > 0:
    A[0] -= 1
    A[1] -= 1
    ans += 1
    A.sort(reverse=True)

print(ans)