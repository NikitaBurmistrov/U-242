def mak(lst):
    if not lst:
        return []

    ml = len(max(lst, key=len))
    ne_lst = []

    for s in lst:
        pa = '_' * (ml - len(s))
        ne_lst.append(s + pa)

    return ne_lst


arr = ["оварлыовар", "фывфывфыв", "Gлврфыовфшыгвп", "фывфвыфвпзщ", "флщафдлао"]
res = mak(arr)

for item in res:
    print(f"'{item}' (len: {len(item)})")