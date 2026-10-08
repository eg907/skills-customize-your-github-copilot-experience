
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. This assignment helps students practice creating a complete game loop while managing hidden words, guesses, and end-of-game logic.

## 📝 Tasks

### 🛠️ Set Up the Game Word and Guess Logic

#### Description
Create the core gameplay loop that chooses a hidden word, accepts player guesses, and updates the current progress as letters are revealed.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Show the hidden word as underscores, such as `_ _ _ _`
- Accept a single letter guess from the player using `input()`
- Reveal matching letters in their correct positions
- Prevent duplicate guesses and keep track of letters already used


### 🛠️ Manage Turns, Incorrect Guesses, and Game End

#### Description
Add the logic for tracking attempts, checking for wins or losses, and ending the game with a clear result message.

#### Requirements
Completed program should:

- Track how many incorrect guesses the player has remaining
- Reduce attempts when a guessed letter is not in the word
- Display feedback after each guess to show progress or errors
- End the game when the full word is guessed correctly
- End the game when the player runs out of attempts
- Print a final message that tells the player whether they won or lost
