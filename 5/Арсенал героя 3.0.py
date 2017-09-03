inventory =["меч", "кольчуга", "щит", "целебное снадобье"]
print("Итак, в вашем арсенале:")
for item in inventory:
    print(item)
input("Нажмите enter, чтобы продолжить")
print("Сейчас в вашем распоряжении", len(inventory),"предмета/-ов.")
input("Нажмите enter, чтобы продолжить ")
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете")

index = int(input("\nВведите индекс одного из предметов арсенала:"))
print("Под индексом",index,"в арсенале находится",inventory[index])
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез inventory[",start,":",finish,"] - это,",end=" ")
print(inventory[start:finish])
input("Нажмите enter, чтобы продолжить")
chest = ["золото","драгоценные камни"]
print("Вы нашли ларец. Вот что в нем есть: ")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу")
inventory += chest
print("Теперт в вашем распоряжении: ")
print(inventory)
input("Нажмите enter, чтобы продолжить.")
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("За золото и драгоценные камни вы купили магический кристалл, cпособный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("теперь в вашем распоряжении: ")
print(inventory)
input("Нажмите enter, чтобы продолжить")
print("в тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в арсеналe: ")
print(inventory)
input("\nНажмите enter, чтобы продолжить")
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print("В арсенале только: ")
print(inventory)
input("\n\nНажмите enter, чтобы выйти.")
