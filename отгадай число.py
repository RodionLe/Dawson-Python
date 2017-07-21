import random
print('\tДобро пожаловать в игру "Отгадай число"!')
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")
the_number = random.randint(1, 100)
guess = int(input("ваше предположение: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    guess = int(input("ваше предположение: "))
    tries = tries + 1
print("Вам удалось отгадать число! Это в самом деле", the_number)
print("Вы затратили на отгадывание всего лишь", tries,"попыток!\n")
input("n\nНажмите enter, чтобы выйти ")
