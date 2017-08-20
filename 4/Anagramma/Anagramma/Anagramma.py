import random
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble =" "
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("""

            Добро пожаловать в игру 'Анаграммы'!
        Надо переставить буквы такб чтобы получить осмысленное слово.
    (Для выхода нажмите enter, не вводя своей версии.)
    """)
print("Вот анаграмма", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению вы не правы.")
    guess = input("\nПопробуйте отгадать исходное слово: ")

if guess == correct:
    print("Да, именно так! Вы отгадали.\n")
print("спасибо за игру.")
input('\n\nНажмите enter, чтобы выйти')

