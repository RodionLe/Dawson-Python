# Демонстрирует обработку исключительных ситуаций
try:
    num = float(input("Введите число "))

except:
    print("Похоже, это не число")

try:
    num = float(input("\nВведите число "))
except ValueError:
    print("Это не число")

# Обработка исключений нескоьких разных типов
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже это не число")

print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки, составленные из цифр!")

# Получение аргумента
try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число! Интерпретатор как бы говорит нам: ")
    print(e)

try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели число ", num)


input("Нажмите enter, чтобы выйти")
        
