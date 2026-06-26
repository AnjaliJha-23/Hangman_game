import random
import hangman_stages
import random_words

print("Welcome to Hangman Game! \nYou have 6 lives to play so be careful!.\nAll the Best and Enjoy!")
lives = 6
choosen_word = random.choice(random_words.words)
print(choosen_word)  # Cheating reveal for testing!

display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)

game_over = False
while not game_over:
    guessed_letter = input('Guess a letter: ').lower()
    
    # 1. Check if the letter matches ANY position in the word
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
            
    # Print the display after checking the whole word
    print(display)
            
    # 2. OUTSIDE the for-loop: Check if the guess was completely wrong
    if guessed_letter not in choosen_word:
        lives -= 1  # Correct way to subtract a life
        print(f"Wrong guess! Lives remaining: {lives}")
        print(hangman_stages.hangman_stages[6 -lives])
        
    
    if lives == 0:
        game_over = True
        print('You Lose!')
        print(f'The correct word was: {choosen_word}')
            
    # 4. Check winning condition
    if '_' not in display:
        game_over = True
        print('You Win!')
    