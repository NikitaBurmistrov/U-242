c = [1,2,3,4,5,6,7,8,0]
s = 0
q = 0
if len(c) == 0:
    print("Пусто")
else:
   for i in range(len(c)):
       s += c[i]
       q += 1

print(s,q)
