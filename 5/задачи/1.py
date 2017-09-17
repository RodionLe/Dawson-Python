import random
words = ["питон","программа", "игра", "приложение", "сериал", "фильм"]
length = len(words)
for i in range (length):
    word = random.choice(words)
    words.remove(word)
    print(word)
