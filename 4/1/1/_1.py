start = int(input("Введите начало осчета: "))
finish = int(input("Введите конец отсчета: "))
a = int(input("Введите интервал отсчета: "))
for i in range(start, finish+1, a):
    print(i)
