# Hangman

A command-line Hangman game in Python, completed as the Stage 8 solution for the [Hyperskill Hangman learning project](https://hyperskill.org/projects/69).

## Run

Requires Python 3. No third-party packages are needed.

```sh
python3 hangman.py
```

## How to play

- Enter `play` to start a round.
- Guess one lowercase English letter at a time.
- Correct guesses reveal every matching letter.
- You have eight lives; each new incorrect letter costs one life.
- Invalid input and repeated guesses do not cost lives.
- Enter `results` at the menu to see wins and losses.
- Enter `exit` at the menu to quit.

The secret word is chosen randomly from `python`, `java`, `swift`, and `javascript`. Scores are kept only during the current program session and reset when the program restarts.

This repository contains a learning-project solution, not an official Hyperskill product.
