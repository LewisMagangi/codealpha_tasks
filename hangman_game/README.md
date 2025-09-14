# Hangman Game - CodeAlpha Internship Project

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

A classic text-based Hangman game implementation in Python, created as part of the CodeAlpha internship program.

## 🎮 Game Description

Hangman is a word guessing game where the player tries to guess a secret word one letter at a time. The player has a limited number of incorrect guesses (6) before the game ends. The game features:

- **5 predefined words**: python, programming, computer, algorithm, codealpha
- **6 maximum incorrect guesses** before game over
- **Visual hangman figure** that progresses with each wrong guess
- **Clear console interface** with game state display
- **Input validation** and error handling
- **Play again functionality**

## 🚀 Features

- ✅ Random word selection from predefined list
- ✅ Visual hangman drawing that updates with wrong guesses
- ✅ Letter tracking (shows guessed letters)
- ✅ Input validation (single letters only)
- ✅ Clear screen between turns for better UX
- ✅ Win/lose detection
- ✅ Play again option
- ✅ Graceful exit handling

## 🛠️ Installation & Setup

1. **Clone/Download the project**:
   ```bash
   git clone https://github.com/YourUsername/CodeAlpha_HangmanGame.git
   cd CodeAlpha_HangmanGame
   ```

2. **Requirements**: 
   - Python 3.6 or higher
   - No external dependencies required (uses only built-in modules)

## 🎯 How to Play

1. **Run the game**:
   
   ```bash
   python hangman.py
   ```

2. **Game Rules**:
   - Guess one letter at a time
   - You have 6 incorrect guesses maximum
   - Letters are case-insensitive
   - Type 'quit' anytime to exit
   - Complete the word before running out of guesses to win!

3. **Example Gameplay**:
  
   ```
   Word: _ _ _ _ _ _
   Guessed letters: None
   Incorrect guesses: 0/6
   Remaining guesses: 6
   
   Enter a letter (or 'quit' to exit): p
   Good guess! 'P' is in the word.
   
   Word: P _ _ _ _ _
   Guessed letters: P
   Incorrect guesses: 0/6
   Remaining guesses: 6
   ```

## 📁 Project Structure

```
hangman_game/
│
├── hangman.py          # Main game file
├── README.md           # Project documentation
└── requirements.txt    # Dependencies (none for this project)
```

## 🔧 Key Python Concepts Demonstrated

This project showcases several important Python programming concepts:

- **Classes and Object-Oriented Programming**: The `HangmanGame` class encapsulates all game logic
- **Random Module**: For random word selection
- **Lists and Sets**: For storing words and tracking guessed letters
- **While Loops**: For main game loop and input validation
- **If-Else Statements**: For game logic and flow control
- **String Manipulation**: For word display and letter checking
- **Input/Output**: Console interaction with user
- **Error Handling**: Try-catch for graceful exits
- **Methods and Functions**: Organized code structure

## 🎨 Game Flow

```
Start Game
    ↓
Select Random Word
    ↓
Display Game State
    ↓
Get Player Input
    ↓
Validate Input
    ↓
Process Guess
    ↓
Update Game State
    ↓
Check Win/Lose Conditions
    ↓
Game Over? → No: Continue Loop
    ↓ Yes
Display Final Result
    ↓
Play Again? → Yes: Reset Game
    ↓ No
End Game
```

## 📝 Code Examples

### Main Game Class Structure:

```python
class HangmanGame:
    def __init__(self):
        self.words = ["python", "programming", "computer", "algorithm", "codealpha"]
        self.max_incorrect_guesses = 6
        self.reset_game()
    
    def play_game(self):
        # Main game loop
        while not self.game_over:
            self.display_game_state()
            guess = self.get_player_guess()
            self.make_guess(guess)
```

### Visual Hangman Display:

```python
def display_hangman(self):
    hangman_figures = [
        # Progressive hangman drawings
        "   ___\n   |  |\n   |\n   |\n   |\n   |\n   =========",
        # ... more figures
    ]
    print(hangman_figures[self.incorrect_guesses])
```

## 🏆 Learning Outcomes

After completing this project, you will have hands-on experience with:
- Python class design and object-oriented programming
- Game loop implementation
- User input handling and validation
- String manipulation and formatting
- Random number generation
- Console application development
- Code organization and documentation

## 🤝 Contributing

This is an internship project, but suggestions and improvements are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share feedback

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 About CodeAlpha

CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This project is part of their Python internship program that empowers students to master Python fundamentals through hands-on projects.

## 📞 Contact

- **Project Creator**: [Your Name]
- **GitHub**: [Your GitHub Profile]
- **LinkedIn**: [Your LinkedIn Profile]
- **Email**: [Your Email]

---

## Happy Coding! 🐍

Built with ❤️ during CodeAlpha Python Internship*