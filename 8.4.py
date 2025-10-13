neob_ekz = {
    "Информатика": 80,
    "Математика": 85,
    "Русский язык": 75
}

print("""Для определения возможности поступления, необходима информация о Вас.
Для inppа ekzа и ballов введите их через |: Химия | 40.
Для завершения inppа нажмите Enter.
""")

sdan_ekz = {}

try:
    while True:
        inpp = input("").strip()
        if inpp == "":
            break
        ekz, ball = [x.strip() for x in inpp.split("|")]
        sdan_ekz[ekz] = int(ball)

    print("Ваши ekzы:")
    for i, (ekz, ball) in enumerate(sdan_ekz.items(), start=1):
        print("{}) {} {}".format(i, ekz, ball))

    ok = True
    for neob_ekz, balls in neob_ekz.items():
        if neob_ekz not in sdan_ekz or sdan_ekz[neob_ekz] < balls:
            ok = False
            break

    print("Вы можете к нам поступить!" if ok else "Увы...")

except ValueError:
    print("Ошибка")
except Exception:
    print("Ошибка")
