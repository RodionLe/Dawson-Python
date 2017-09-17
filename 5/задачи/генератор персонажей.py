x = 0
strength = 0
agility = 0
health = 0
wisdom = 0
choice = None
while choice != 0:
    print("""Вы можете распределить свои пункты между четырьмя характеристиками.
        1 - сила
        2 - здоровье
        3 - мудрость
        4 - ловкость
        5 - перераспределить характеристики
        6 - выйти из меню
        7 - посмотреть характеристики
                """)
    choice = input("Ваш выбор: ")
    if choice == "1" and x != 30:
        strength += 1
        x += 1
    if choice == "2" and x != 30:
       health += 1
       x += 1
    if choice == "3" and x != 30:
        wisdom += 1
        x += 1
    if choice == "4" and x != 30:
        agility += 1
        x += 1
    if choice == "5":
        x = 0
        strength = 0
        agility = 0
        health = 0
        wisdom = 0
    if choice == "6":
        break
    if choice == "7":
        print("Ваши характеристики.")
        print("Сила", strength)
        print("здоровье", health)
        print("мудрость", wisdom)
        print("ловкость", agility)
    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        print("извините, в меню нет пункта", choice)
print("Ваши характеристики.")
print("Сила", strength)
print("здоровье", health)
print("мудрость", wisdom)
print("ловкость", agility)        
print("Хотите ли вы перераспределить свои характеристики ?")
