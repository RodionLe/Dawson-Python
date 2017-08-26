import random 
i = 0
WORDS = ("питон", "программа")
word = random.choice(WORDS)
print("""          Добро пожаловать в игру 'угадай слово'.
          Вам нужно угадать слово, которое загадал наш компьютер.
        У вас будет пять попыток узнать, есть ли какая-либо буква в слове.
        """)
print("Букв в слове - ",len(word))

for i in range(5):
    a = input("Введите букву: ")
    if a in word:
        print("Да")
    else:
        print("нет")
answer = input("Ваш ответ: ")
if answer == word:
    print("Поздравляю! Вы победили.")
else:
    print("YOU LOSE")