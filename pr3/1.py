team = input("")

print(team, "- чемпион!")
print("-" * len(team))

team_l = team.lower()
print( len(team))
print('п' in team_l)
print(team_l.count('а'))


#2
a = input("Государство ")
b = input("Столица")

print("Государство ", a + ", столица ", b)


#3
s = "объектно-ориентированный"

print(s[0:6])
print(s[9:18])
print(s[15:18])
print(s[2:5])
print(s[6:11])


#4
st = input("Введите строку: ")
su = input("Введите подстроку: ")

if st.lower() in st.lower():
    print("Есть")
else:
    print("Нет")


#5
a1 = input("")
b1 = input("")

if b1 in a1:
    print("Первое", a1.find(b1))
    print("Последнее", a1.rfind(b1))
else:
    print("Нет")



#6
text = input("")

text = text.replace(" ", "")

chas = {}
for ch in text:
    chas[ch] = chas.get(ch, 0) + 1

top3 = []
for _ in range(3):
    if not chas:
        break
    max_ch = max(chas, key=chas.get)
    top3.append((max_ch, chas[max_ch]))
    del chas[max_ch]

# выводим
for sym, count in top3:
    print(sym, "-", count)


