import random 
i = 0
WORDS = ("питон", "программа")
word = random.choice(WORDS)
length = len(word)
tries = '*' * length



print("""          Добро пожаловать в игру 'угадай слово'.
          Вам нужно угадать слово, которое загадал наш компьютер.
        У вас будет пять попыток узнать, есть ли какая-либо буква в слове.
        """)
print("Букв в слове - ", length)

for i in range(5):
    a = input("Введите букву: ")
    if a in word:
        print("Да")
        for i in range(length):
            if a == word[i]:
                 tries =  tries[:i] + a + tries[i+1:]
        print(tries)
    else:
        print("нет")

for i in range(5):
    answer = input("Ваш ответ: ")
    if answer == word:
        print("Поздравляю! Вы победили.")
        break
    else:
        print("YOU LOSE")
