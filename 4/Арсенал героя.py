inventory = ()
if not inventory:
    print("Вы безоружны.")
input("\nНажмите enter, чтобы продолжить")
inventory = ("Меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\nСодержание кортежа: ")
print(inventory)
print("\nИтак, в вашем арсенале: ")
for item in inventory:
    print(item)
input("\n\nНажмите enter, чтобы выйти")
