N, K = map(int, input().split())
A = list(map(int, input().split()))

# for _ in range(K):
#     A.insert(0, A.pop())

ans = A[N - K :] + A[: N - K]
print(*ans)
