x = int(input("Введите число от 1 до 10: "))
if x == 1:
    print("Число верно")
elif x == 0 or x == 11:
    print("ошибка")
else:
    print("Число неверно")
    y = int(input("Продолжить? 1 - да 2 - нет"))
    if y == 1:
        x = int(input("Введите число от 1 до 10: "))
        if x == 1:
            print("Число верно")
        elif x == 0 or x == 11:
            print("ошибка")
    else:
        print(" ")

