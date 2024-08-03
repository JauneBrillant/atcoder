n = int(input())
odds = [num for num in range(1, n + 1) if num % 2 != 0]

ans = 0
for num in odds:
    divisor_cnt = lambda num: sum(1 for i in range(1, num + 1) if num % i == 0)
    if divisor_cnt(num) == 8:
        ans += 1

print(ans)
