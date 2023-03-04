import random
import hangmanart
def play_hangman():

    word_list = ["pablo", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    letters = []
    print(chosen_word)
    guess_l = ["_" for _ in chosen_word]
    print(" ".join(guess_l))
    lives = 7

    while True:
        guess = input("Guess a letter: ").lower()
        if guess in letters:
            print("Letter already used!")
        else:    
            if guess not in chosen_word:
                print(hangmanart.stages[lives-1])
                lives -= 1
            else:
                for index, letter in enumerate(chosen_word):
                    if letter == guess:
                        guess_l[index] = guess   
        print(" ".join(guess_l))
        letters.append(guess)
        if lives == 0:
            print("LOSER")
            break
        if "_" not in guess_l:
            print("WINNER")
            break

play_hangman()
