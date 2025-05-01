from wonderwords import RandomWord
import hangmanwordbank as h
r = RandomWord()
word = r.word()
letters = list(word)
letter_num = len(letters)
underscores = ['_'] * letter_num
lives = 6
guessed = set()
game_over = False
hwb_count = 0

def dash():
    print(''.join(underscores))

while not game_over:
    print("Word to guess: ", end = " ")
    dash()
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("You've already guessed")
        continue

    guessed.add(guess)

    if guess in letters:
        for i,letter in enumerate(letters):
            if letter == guess:
                underscores[i] = guess
        letter_num -= letters.count(guess)
        print(h.hwb[hwb_count])
        print("**************************** " + str(lives) + "/6 LIVES LEFT****************************")
    else:
        lives -= 1
        hwb_count += 1
        print(h.hwb[hwb_count])
        print("You guessed " + guess + ", that's not in the word. You lose a life.")
        if lives > 0:
            print("**************************** " + str(lives) + "/6 LIVES LEFT****************************")

    if letter_num <= 0:
        print("**************************** IT WAS " + word + "! YOU WIN ****************************")
        game_over = True
    elif lives <= 0:
        print("**************************** IT WAS " + word + "! YOU LOSE ****************************")
        game_over = True
