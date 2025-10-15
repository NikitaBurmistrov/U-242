try:
    with open('x.txt', 'r') as f:
        nums = []
        for line in f:
            try:
                num = float(line.strip())
                nums.append(num)
            except ValueError:
                continue

    if not nums:
        print("Нет чисел в файле.")
    else:
        s = sum(nums)
        m = max(nums)

        with open('x.txt', 'a') as f:
            f.write(f"{s}\n")
            f.write(f"{m}\n")

        print(f"сумма {s}")
        print(f"максимум {m}")

except FileNotFoundError:
    print("файл не найден")
except Exception as e:
    print(f"ошибка: {e}")