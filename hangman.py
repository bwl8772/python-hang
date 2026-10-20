import random

words = ["python", "java", "swift", "javascript"]
wins = 0
losses = 0

print("H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if choice == "exit":
        break
    if choice == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
        continue
    if choice != "play":
        continue

    secret_word = random.choice(words)
    guessed_letters = set()
    lives = 8
    while lives > 0:
        print()
        hidden_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "-"
        print(hidden_word)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if not "a" <= guess <= "z":
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue
        guessed_letters.add(guess)
        if guess not in secret_word:
            print("That letter doesn't appear in the word.")
            lives -= 1
        elif set(secret_word).issubset(guessed_letters):
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            wins += 1
            break
    else:
        print("\nYou lost!")
        losses += 1
    print()
