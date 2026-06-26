# 🎮 Interactive Hangman Game

A classic command-line Hangman game built using Python. The game selects a random word from a library, tracks player lives, accepts input, and displays real-time ASCII hangman art that builds up piece-by-piece as incorrect guesses are made.

---

## ✨ Features

* **Dynamic Word Selection:** Randomly chooses words from an external module on every new game.
* **Interactive Terminal Interface:** Updates your guessed progress (e.g., `_ _ _`) instantly.
* **Progressive ASCII Art:** Features a 6-stage visual hangman that constructs dynamically based on remaining lives.
* **Input Validation:** Automatically normalizes guesses to lowercase letters.

---

## 🛠️ Project Structure

The repository consists of the following core files:
* `hangman_game.py` - The main game loop containing the core logic and user input handling.
* `random_words.py` - Module containing the collection of words used for the game.
* `hangman_stages.py` - Module containing the multi-line ASCII strings representing the hangman stages.

---

## 🚀 How to Run the Game

### Prerequisites
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine.

### Execution Steps
1. Clone this repository to your local computer:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Hangman_game.git](https://github.com/YOUR_USERNAME/Hangman_game.git)

```

2. Navigate into the project folder:
```bash
cd Hangman_game

```


3. Run the main game file:
```bash
python hangman_game.py

```



---

## 🎮 How to Play

1. When the game starts, you will see blank blanks (`_`) corresponding to the length of the chosen hidden word.
2. You start with **6 lives**.
3. Type a single letter into the terminal and press `Enter`.
* **Correct Guess:** The letter replaces the blank underscore in its correct positions.
* **Incorrect Guess:** You lose 1 life, and a part of the hangman is drawn.


4. Fill out the entire word to **Win** 🎉. If the hangman is completely drawn before you guess the word, you **Lose** 💀.




