print("Варіант 13 - число Армстронга. Машир А. М. КМ-93")
n = int(input("Введіть число "))
number = 1
def armst():
    global number
    sum = 0
    List = list(str(number))
    L = len(List)
    for i in List:
        sum += (int(i) ** L)
    if number == sum:
        print(str(sum) + " є числом Армстронга")
    number += 1
    return number
while number <= n:
    armst() 