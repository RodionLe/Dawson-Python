a = input("Введите текст: ")
x = len(a)
for i in range(int(x)):
    y = a[(x) -1 - i]
    print(y,end="")
input("\n\nНажмите enter,чтобы выйти")