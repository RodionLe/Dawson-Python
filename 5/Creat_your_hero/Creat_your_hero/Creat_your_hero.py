person = [0, 0, 0, 0]
Power = 0
gility = 0
Health = 0 
Knowlage = 0
choice1 = None
i = 30 
sumDOSTUPNpoints = 30

def print_char_menu():
    print(
            """
            0 - Ловкость
            1 - Сила 
            2 - Здоровье 
            3 - Мудрость
            """)
    characteristic = int(input())
    if characteristic >= len(person):
        print("Некорректный ввод")
        return False
    else:
        return characteristic

def del_char():
    global sumDOSTUPNpoints

    print("От какой характеристике вы хоттите отнять очки?")
    characteristic = print_char_menu()

    if characteristic == False:
        return False
    else:
        characteristicValue = int(input("Введите, сколько очков:"))
        if characteristicValue > person[characteristic]:
            sumDOSTUPNpoints += person[characteristic]
            person[characteristic] = 0
        else: 
             person[characteristic] -= characteristicValue
             sumDOSTUPNpoints += characteristicValue
        return sumDOSTUPNpoints

def add_char():
    global sumDOSTUPNpoints

    print("К какой характеристике вы хоттите лобавить очки?")
    characteristic = print_char_menu()
       
    if characteristic != False:
        characteristicValue = int(input("Введите, сколько очков:"))
        if characteristicValue > sumDOSTUPNpoints: 
             person[characteristic] += sumDOSTUPNpoints
             sumDOSTUPNpoints = 0
        else: 
             person[characteristic] += characteristicValue
                
             sumDOSTUPNpoints -= characteristicValue 
        return sumDOSTUPNpoints

def print_hero_info(person):
    print("Ваша характеристика: ")
    print("Ловкость - ","*" * person[0])
    print("Сила - ","*" * person[1])
    print("Здоровье -","*" * person[2])
    print("Мудрость -","*" * person[3])

def creat_your_hero():
    choice = None
    while choice != 0:
        print(
        """
        0 - Выйти
        1 - Добавить характеристку
        2 - Убрать пункты характреристики
        3 - Посмотреть характеристику
        """)
        choice = input("Введите цифру: ")
        if choice == "1":
            sumDOSTUPNpoints = add_char()
            print("Осталось очков: ", sumDOSTUPNpoints)
        elif choice == "2":
            sumDOSTUPNpoints = del_char()
            print("Осталось очков: ", sumDOSTUPNpoints)
        elif choice == "3":
            print_hero_info(person)
        elif choice == "0":
            return
        else :
            print("До свидания.")

x = 1
while x > 0:
    creat_your_hero()
    x = int(input("Если вы хотите создать нового персонажа введите '1', если нет, то '0'"))
    if x == 0:
        break



 
    