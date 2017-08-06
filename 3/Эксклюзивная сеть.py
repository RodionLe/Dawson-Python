print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегестрированных пользователей!\n")
security = 0
username = ""
while not username:
    username = input("Логин: ")
password = ""
while not password:
    password = input("Пароль: ")
if username == "Родион" and password == "секрет":
    print("привет, Родя")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Здравствуй, Сид")
    security = 3
elif username == "guest" or password == "guest":
    print("Добро пожаловать к нам в гости")
    security = 1
else:
    print("Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гражданин.\n")
input("\n\nНажмите enter, чтобы выйти")
