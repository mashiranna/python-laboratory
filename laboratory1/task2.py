print("Варіант 13 - перевірка правильності дати, введеної з клавіатури. Машир А. М. КМ-93")
day = int(input("Введіть число"))
month = int(input("Введіть місяць"))
if 1<=day<=31 and 1<=month<=12:
    print("Введені коректні дані")
else: print("Введені некоректні дані")