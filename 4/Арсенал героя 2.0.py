inventory = ("Меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\nИтак, в вашем арсенале: ")
for item in inventory:
    print(item)
input("\n\nНажмите enter, чтобы продолжить.")
print("Сейчас в вашем распоряжении", len(inventory),"Предмета/-ов.")
input("\n\nНажмите enter, чтобы продолжить.")
if "целебное снадобье" in inventory:
    print("Вы еще повоюете.")
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом",index,"в арсенале находится",inventory[index])
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("\nВведите конечный индекс среза: "))
print("срез inventory[",start,":",finish,"]-это",end =" ")
print(inventory[start:finish])
input("\nНажмите enter,тобы продолжить")
chest = ("золото","драгоценные камни")
print("Вы нашли ларец. Вот что в нем есть: ")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("\n\nНажмие enter, чтобы выйти")
