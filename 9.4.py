with open('stih.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
    ws = text.split()
    glas = 'аеёиоуыэюя'
    glass= sum(1 for w in ws if w and w[0] in glas)
    soglass = sum(1 for w in ws if w and w[0] not in glas)

    print(text)
    print(f"глассных {glass}")
    print(f"согласных {soglass}")
    if glass > soglass:
        print("Больше глассных")
    elif soglass > glass:
        print("Больше согласных")
    else:
        print("Одинаково")