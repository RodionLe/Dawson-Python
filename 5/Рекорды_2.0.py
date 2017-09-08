scores = []
choice = None
while choice != "0":
    print("""
        Рекорды 2.0

        0 - Выйти
        1 - Показать рекорд
        2 - Добавить рекорд
        """)
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРезультат")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:5] #в списке остается только 5 рекордов
    else:
        print("Извините, в меню нет пункта", choice)
input("\n\nНажмите enter, чтобы выйти.")
        
