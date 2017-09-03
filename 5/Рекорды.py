scores = []
choise = None
while choise != "0":
    print("""
    Рекорды
    0 - выйти
    1 - показать рекорды
    2 - добавить рекорд
    3 - удалить рекорд
    4 - сортировать список
    """)
    choise = input("Ваш выбор ")
    print()
    if choise == "0":
        print("До свидания")
    elif choise == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    elif choise == "2":
        score = int(input("Введите свой рекорд"))
        scores.append(score)
    elif choise == "3":
        score = int(input("какой из рекордов удалить ?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат",score,"не находится в списке")
    elif choise == "4":
        scores.sort(reverse = True)
    else:
        print("извините, в меню нет пункта",choise)
input("Нажмите enter, чтобы выйти")
