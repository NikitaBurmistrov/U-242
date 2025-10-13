try:
    n = int(input())
    middle_names = {}
    count = 0
    for i in range(n):
        fio = input("Фио ").split()
        if len(fio) == 3:
            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
            count += 1
    if middle_names:
        print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
    else:
        print("Отчеств нет")
    print("Столько участвовало", count)
except ValueError:
    print("Ошибка ввода")
