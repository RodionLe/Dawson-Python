import random
print("Загадайте число от 1 до 100")
x = int(input("Введите число "))
y = 50
z = 25
while x != y:
    if y > x:
        print(y, "больше искомого")
        y = y - z
    else:
        print(y, "меньше искомого")
        y = y + z
    z = z // 2
print(y)
