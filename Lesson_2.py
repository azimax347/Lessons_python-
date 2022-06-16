x = int(input("Число\"x\": "))
y = int(input("Число\"y\": "))

name_1 = x + y
name_2 = x - y
name_3 = x * y
name_4 = x / y
name_5 = x // y
name_6 = x ** y
name_7 = x % y
print(f"Сложение: {name_1}, Вычитание: {name_2}, Умножение: {name_3},"
      f" Деление: {name_4}, Целочисленное деление: {name_5},"
      f" Возведение в степень: {name_6}, Остаток от деления: {name_7}")
print(f"Число {name_4} округленное до 2 знаков после запятой: {round(name_4,2)}")
print(f"{name_6} в двоичной системе {name_6:0b}")
name_8 = x & y
name_9 = x | y
name_10 = x ^ y
name_11 = ~x
name_12 = x << y
name_13 = x >> y
print(f"Логическое умножение {x:0b} и {y:0b}: {name_8:0b}\n"
      f"Логическое Сложение {x:0b} и {y:0b}: {name_9:0b}\n"
      f"логическое исключающее ИЛИ {x:0b} и {y:0b}: {name_10:0b}\n"
      f"логическое не {x:0b}: {name_11:0b}\n"
      f"Логический сдвиг {x:0b} влево на {y:0b}: {name_12:0b}\n"
      f"Логическй сдвиг {x:0b} вправо на {y:0b}: {name_13:0b}\n")
