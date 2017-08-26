import random
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble =" "
help = word[0]
x = 0
points = 1000
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("""

            Добро пожаловать в игру 'Анаграммы'!
        Надо переставить буквы такб чтобы получить осмысленное слово.
    (Для выхода нажмите enter, не вводя своей версии.)
    (У вас есть одна подсказка)
    (Чтобы воспользоваться подсказкой напишите 'подсказка')
    """)
print("Вот анаграмма", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению вы не правы.")
    if guess == 'подсказка' and x == 0:
       x += 1
       print('Первая буква - ',help)
    guess = input("\nПопробуйте отгадать исходное слово: ")
if x == 1:
    points -= 100
if guess == correct:
    print("Да, именно так! Вы отгадали.\n")
print("спасибо за игру. Вы получили",points,"очков")
input('\n\nНажмите enter, чтобы выйти')

