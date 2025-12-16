import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baleia", "camelo", "doninha", "elefante",
             "flamingo", "galinha", "hiena", "iguana", "jararaca",
             "kiwi", "lince", "morsa", "narval", "ovelha", "papagaio",
             "quati", "rinoceronte", "suricate", "tartaruga", "urso",
             "vagalume", "wallaby", "ximango", "yak", "zebra"]

chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display += "_"


game_over = False
lives = 6
while game_over is not True:
    i = -7 + lives
    print(stages[i])
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    print(display)

    if lives == 0:
        game_over = True
        print(stages[0])
        print(f"You Lose! The word is {chosen_word}.")
    if not "_" in display:
        game_over = True
        print("You win!")
    if game_over:
        break
