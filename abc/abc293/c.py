H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)


def solve(i, j, visited):
    global ans
    if A[i][j] in visited:
        return
    visited.add(A[i][j])

    if i == H - 1 and j == W - 1:
        ans += 1

    if i + 1 < H:
        solve(i + 1, j, visited)
    if j + 1 < W:
        solve(i, j + 1, visited)

    visited.remove(A[i][j])


ans = 0
visited = set()
solve(0, 0, visited)
print(ans)
