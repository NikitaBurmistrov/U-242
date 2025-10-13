a = 12
b = 20

mn = min(a, b)
mx = max(a, b)

for i in range(mn, mx + 1):
    print(i, end=" ")
print()

for i in range(mx, mn - 1, -1):
    print(i)
