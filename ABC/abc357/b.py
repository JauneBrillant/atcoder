s = input()

u = sum(c.isupper() for c in s)
l = sum(c.islower() for c in s)
print(s.upper() if u > l else s.lower())
