#словари, ключ - значение
geek = {"404": "не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
        "Googling" : "'Гугление', поиск в Сети сведений о ком-либо.",
        "Keyboard Plaque" : "Мусор, который скапливается в клавиатуре компьютера.",
        "Link Rot" : "Процесс устаревания гиперссылок на веб-страницах.",
        "Percussive Maintenance" : "О ситуации, когда кто-либо бьет по корпусу неисправного электро прибора в надежде воссиановить его работу.",
        "Uninstalled" : "б увольнении кого-либо. Особенно популярно на рубеже 1990 - 2000-х годов."}
if "Dancing Baloney" in geek:
    print("Я знаю, что такое Dancing Baloney")
else:
    print("Я понятия не имею, что такое Dancing Baloney")
choice = None
while choice != "0":
    print("""
        Переводчик с гикского на русский

        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - изменить толкование
        4 - удалить термин
        """)
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        term = input("Какой термин вы хотите перевести с гикского на русский? ")
        if term in geek:
            definition = geek[term]
            print("\n",term,"означает", definition)
        else:
            print("\nУвы, такой термин мне не знаком", term)
    elif choice == "2":
        term = input("Какой термин вы хотите добавить? ")
        if term not in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term,"добавлен в словарь")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить толкование")
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition = input("Впишите ваше толкование: ")
            geek[term] = definition
            print("\nТермие",term,"переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")
    elif choice == "4":
        term = input("Какой термие вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин",term,"удален")
        else:
            print("\nНичем не могу помочь. Термина", term,"нет в словаре")
    else:
        print("Извините, в меню нет пункта", choice)
input("Нажмите enter, чтобы выйти")
