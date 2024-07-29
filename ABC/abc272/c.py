n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)


def is_even(num):
    return num % 2 == 0


evens = []
odds = []
for num in a:
    if is_even(num):
        evens.append(num)
    else:
        odds.append(num)

evens.sort(reverse=True)
odds.sort(reverse=True)

ans = -1
if len(evens) >= 2:
    ans = max(ans, evens[0] + evens[1])
if len(odds) >= 2:
    ans = max(ans, odds[0] + odds[1])

print(ans)
