n = 100

divisor = []

i = 1
while i * i <= n:
    if n % i == 0:
        divisor.append(i)
        divisor.append(n // i)
    i += 1

print(divisor)
