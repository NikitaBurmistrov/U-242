t = (3, 1, 7, 2)
if all(isinstance(i, int) for i in t):
    t = tuple(sorted(t))
print(t)
