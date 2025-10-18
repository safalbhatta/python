import random

word_bank = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'go', 'rust']
word = random.choice(word_bank)
guessedWord = ['-'] * len(word)
attempts = 10

print("Welcome to Guess the Word!")

while attempts > 0:
    print("\n" + ''.join(guessedWord))
    guess = input("Input a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Incorrect! Attempts left:", attempts)

    if '-' not in guessedWord:
        print("\n" + ''.join(guessedWord))
        print("Congratulations! You've guessed the word.")
        break

if attempts == 0 and '-' in guessedWord:
    print("Sorry, you've run out of attempts. The word was:", word)