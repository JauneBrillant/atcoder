n = int(input())

divisor = set()

i = 1
while i * i <= n:
    if n % i == 0:
        divisor.add(i)
        divisor.add(n // i)
    i += 1

sorted = sorted(divisor)
for v in sorted:
    print(v)
