p = float(input())
massa = [float(x) for x in input().split()]
massa1 = sum(massa)
if massa1 <= p:
    print("возможна")
else:
    print("невозможна")
