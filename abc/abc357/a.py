n, m = map(int, input().split())
h = list(map(int, input().split()))

ans = sum(1 for hand in h if (m := m - hand) >= 0)
print(ans)
