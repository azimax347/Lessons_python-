x = 0
while x < 10:
    print(f" {x}  ")
    x += 1
else:
    print(f"Значение после основного условия = {x}")
print("Цикл WHILE завершён \n")

for y in range(10):
    print(f"Test {y}")
print("Цикл FOR завершён")

for x in range(1, 11):
    for y in range(1, 10):
        print(x * y, end="\t")
    print("\n")
