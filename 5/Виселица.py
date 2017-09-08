import random
HANGMAN = ("""
    _________
   |       | 
   |       |
   |
   |
   |
   |
   |
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  |
   |
   |
   |
   |
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  |  -+-
   |
   |
   |
   |
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  | /-+-
   |
   |
   |
   |
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  | /-+-/
   |       
   |        
   |        
   |      
   |      
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  | /-+-/
   |       |
   |        
   |        
   |      
   |      
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |       O  | /-+-/
   |       |
   |       | 
   |       | 
   |      | 
   |      | 
   |
   |
   |
   |
   _____________
   """,
           """
    _________
   |       | 
   |       |
   |    |  O  | /-+-/
   |     \ | / 
   |       | 
   |       | 
   |      | |
   |      | |
   |
   |
   |
   |
   _____________
   """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ПИТОН", "ПРОГРАММА", "ИГРА")
word = random.choice(WORDS) #слово для отгадывания
so_far = "-" * len(word) # дефисы
wrong = 0 # количество ошибок
used = [] # буквы, которые уже были
print("Добро пожаловать в игру 'Bиселица'. Удачи вам")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже продполагали следующие буквы:\n",used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже продполагали букву", guess)
        guess = input("\n\nВведите буву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nДа! Буква", guess,"есть в слове")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, буквы", guess,"нет в слове.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили")
else:
    print("\nВы отгадали!")
print("\nБыло загадано слово", word)
input("\n\nНажмите enter, чтобы выйти")
