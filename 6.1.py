info = {}
info["фио"] = "Бурмистров Никита Викторович"
info["дата_рождения"] = "08/11/2006"
info["место_рождения"] = "Калуга"

print(info)

info["хобби"] = ["Аналитика Dota 2", "чтение классической литературы"]
info["хобби"].append("математика")

info["животные"] = ("кот Груша",)

info["ЕГЭ"] = {}
info["ЕГЭ"]["Математика"] = 82
info["ЕГЭ"]["Информатика"] = 85
info["ЕГЭ"]["Русский язык"] = 66
info["ЕГЭ"]["Физика"] = 0
del info["ЕГЭ"]["Физика"]

info["вузы"] = {}
info["вузы"]["МГУ"] = 270
info["вузы"]["МФТИ"] = 290
info["вузы"]["ВГУИТ"] = 190

print("Данные:")
print(info)

exam = ", ".join(sorted(info["ЕГЭ"].keys()))
print("Предметы:", exam)

vuzi = ", ".join(sorted(info["вузы"].keys()))
print("Вузы:", vuzi)

print("Ответы на вопросы:")
name = info["фио"].split()[1]
starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info["дата_рождения"].split("/")[1])
born_in_winter_or_summer = month in [12, 1, 2, 6, 7, 8]
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"])))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = sum(int(sum_mark >= value) for value in info["вузы"].values())
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))
