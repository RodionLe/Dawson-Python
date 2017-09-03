a = input("Введите текст: ")
x = len(a) - 1
for i in range(x + 1):
    print(a[x - i], end="")
input("\n\nНажмите enter,чтобы выйти")
