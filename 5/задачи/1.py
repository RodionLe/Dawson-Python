import random
words = ["питон","программа", "игра", "приложение", "сериал", "фильм"]
length = len(words)
Newwords = []
for i in range(length):
    word = random.choice(words)
    Newwords.append(word)
    words.remove(word)
print(Newwords)
