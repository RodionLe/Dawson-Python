family = {"Аркадий Кирсанов": "Николай Кирсанов",
          "Евгений Базаров": "Василий Базаров",
          "Петр": "Алексей Михайлович",
          "Люк": "Энакин"}
choice = None
while choice != "0":
    print("""
            Вас приветствует программа "Кто твой папа."
            Введите имя персонажа, если хотите узнать, кто его отец.

            0 - выйти
            1 - узнать отца
            2 - добавить пару
            3 - изменить пару
            4 -удалить пару
            """)
    choice = input("Ващ выбор\n ")
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        name = input("Введите имя ")
        if name in family:
            father = family[name]
            print("у", name,"отцом является :",father)
        else:
            print("Увы, такой пары у нас нет.")
    elif choice == "2":
        name = input("Введите пару, которую хотите добавить ")
        if name not in family:
            father = input("Введите отца")
            family[name] = father
            print("Пара добавлена")
        else:
            print("Такая пара уже есть")
    elif choice == "3":
        name = input("Введите пару, которую хотите изменить ")
        if name in family:
            father = input("Введите имя отца")
            family[name] = father
        else:
            print("Такой пары нет.")
    elif choice == "4":
        name = input("Введите имя, кторое хотите удалить ")
        if name in family:
            del family[name]
            print("Пара", name ,"удалена")
        else:
            print("Такой пары нет")
    else:
        print("В меню нет пункта", choice)
input("Нажмите enter, чтобы выйти")
            
