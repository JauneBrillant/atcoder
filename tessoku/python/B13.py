n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
res = 0
j = 0
for i in range(n):
    print("\ni == " + str(i))
    while j < n and sum + a[j] <= k:
        sum += a[j]
        j += 1
        print("sum = " + str(sum))
    print("j - i == " + str(j - i))
    res += j - i
    sum -= a[i]

print(res)
