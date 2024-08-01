N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

start = A[len(A) // 2]
end = B[len(B) // 2]

ans = 0
for i in range(N):
    ans += abs(A[i] - start)
    ans += abs(A[i] - B[i])
    ans += abs(B[i] - end)

print(ans)
