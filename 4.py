from math import prod

a = []
b = []
a.append(4.5)
a.append(3.4)
a.extend([8.7, 1.3])
b.append(14.5)
b.append(3.4)
b.extend([8.7, 11.3])
a.insert(1, 100)
a.insert(3, 100)
b.insert(0, 200)
b.insert(2, 200)
print("Исхо")
print("1-й:", a)
print("2-й:", b)
del a[0]
del b[0]
a.remove(100)
b.remove(200)

print(a)
print(b)
sa = set(a)
sb = set(b)
sab = sa & sb

print(sa)
print(sb)
print(sab)
c = a + b
asc = sorted(c)
desc = sorted(c, reverse=True)
ar = sum(c[1::2]) / len(c[1::2])

geom = pow(prod(c[::2]), 1/len(c[::2]))
mx = max(c)
mn = min(c)

print(c)
print("возр", asc)
print("убыв", desc)
print(f"{ar} {geom}")
print("Макс. и мин.:", mx, mn)