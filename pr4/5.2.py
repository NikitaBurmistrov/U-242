t = (1, 2, 3, 4, 5, 3, 6)
x = 3
if x not in t:
    res = ()
else:
    a = t.index(x)
    if t.count(x) > 1:
        b = t.index(x, a + 1)
        res = t[a:b + 1]
    else:
        res = t[a:]
print(res)
