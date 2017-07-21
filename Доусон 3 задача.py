import random
print('\tДобро пожаловать в игру "Отгадай число"!')
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
tries = int(input("Введите количество попыток за которые вы сможете отгадать число "))
the_number = random.randint(1, 100)
guess = int(input("ваше предположение: "))

while tries != 0:
    tries -= 1
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    guess = int(input("ваше предположение: "))
    if guess == the_number:
        print("Вы победили")
        break
    elif tries == 1:
        print("Вы проиграли")
        break
     
               

