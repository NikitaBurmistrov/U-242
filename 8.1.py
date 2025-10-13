def ceasar(text, shift):
    lett = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    try:
        text = str(text).lower()
        shift = int(shift)
        encoded = ""
        for ch in text:
            if ch in lett:
                encoded += lett[(lett.index(ch) + shift) % len(lett)]
            else:
                encoded += ch
        decoded = ""
        for ch in encoded:
            if ch in lett:
                decoded += lett[(lett.index(ch) - shift) % len(lett)]
            else:
                decoded += ch
        print("Зашифрованная строка:", encoded)
        print("Расшифрованная строка:", decoded)
    except (ValueError, TypeError, IndexError):
        print("Ошибка")

ceasar("ываываываываываыва", 3)
