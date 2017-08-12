word = "пицца"
print("Ведите начальный и конечный индекс для того среза 'пиццы',который хотите получить.")
print("Для входа нажмите enter, не вводя начальную позицию. ")
start = None
while start!="":
    start = (input("\nНачалььная позиция: "))
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("срез word[",start,":",finish,"] выглядит как",end=" ")
        print(word[start:finish])
input("Нажмите enter, чтобы выйти")
