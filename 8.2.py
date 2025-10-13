def power(x, y=2):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

try:
    x = int(input())
    y = int(input())
    print(power(x, y))
except ValueError:
    print("Ошибка числовая")
except TypeError:
    print("Ошибка типа данных")
except RecursionError:
    print("Рекурсия")
