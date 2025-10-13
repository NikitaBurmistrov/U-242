lst = [1,2,3,4,5,6,6,66,6,6,6,6,6,6,6,]
s = 'ldkajsdlakhsd'


def f(x):
    c = set()
    for i in range(len(x)):
        c.add(s[i])
    return c

print(f(s),len(f(s)))
print(f(lst),len(f(lst)))