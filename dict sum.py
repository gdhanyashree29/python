n = int(input("Enter n: "))

d = {}

for i in range(1, n + 1):
    d[i] = i * i

print("Dictionary:", d)

total = 0
for v in d.values():
    total += v

print("Sum of values:", total)
