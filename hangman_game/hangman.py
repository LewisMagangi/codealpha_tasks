#!/usr/bin/env python3
"""
Hangman Game - CodeAlpha Python Internship Project
==================================================

A simple text-based Hangman game where the player guesses a word one letter at a time.

Author: CodeAlpha Intern
Date: September 2025
"""

import random
import os


class HangmanGame:
    """A class to represent the Hangman game."""
    
    def __init__(self):
        """Initialize the game with predefined words and game settings."""
        self.words = ["python", "programming", "computer", "algorithm", "codealpha"]
        self.max_incorrect_guesses = 6
        self.reset_game()
    
    def reset_game(self):
        """Reset the game state for a new game."""
        self.word = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.game_over = False
        self.won = False
    
    def display_hangman(self):
        """Display the hangman figure based on incorrect guesses."""
        hangman_figures = [
            """
            ___
            |  |
            |
            |
            |
            |
            =========""",
            """
            ___
            |  |
            |  O
            |
            |
            |
            =========""",
            """
            ___
            |  |
            |  O
            |  |
            |
            |
            =========""",
            """
            ___
            |  |
            |  O
            | /|
            |
            |
            =========""",
            """
            ___
            |  |
            |  O
            | /|\\
            |
            |
            =========""",
            """
            ___
            |  |
            |  O
            | /|\\
            | /
            |
            =========""",
            """
            ___
            |  |
            |  O
            | /|\\
            | / \\
            |
            ========="""
        ]
        
        if self.incorrect_guesses < len(hangman_figures):
            print(hangman_figures[self.incorrect_guesses])
    
    def display_word(self):
        """Display the word with guessed letters revealed and others as underscores."""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def display_game_state(self):
        """Display the current game state."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        
        print("=" * 50)
        print("        🎮 HANGMAN GAME - CodeAlpha 🎮")
        print("=" * 50)
        
        self.display_hangman()
        
        print(f"\nWord: {self.display_word()}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
        print(f"Remaining guesses: {self.max_incorrect_guesses - self.incorrect_guesses}")
    
    def is_word_guessed(self):
        """Check if the entire word has been guessed."""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def make_guess(self, letter):
        """Process a letter guess."""
        letter = letter.upper()
        
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'. Try a different letter!")
            return False
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            if self.is_word_guessed():
                self.won = True
                self.game_over = True
        else:
            print(f"Sorry! '{letter}' is not in the word.")
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                self.game_over = True
        
        return True
    
    def get_player_guess(self):
        """Get and validate player's letter guess."""
        while True:
            try:
                guess = input("\nEnter a letter (or 'quit' to exit): ").strip()
                
                if guess.lower() == 'quit':
                    return 'quit'
                
                if len(guess) != 1:
                    print("Please enter exactly one letter!")
                    continue
                
                if not guess.isalpha():
                    print("Please enter a valid letter!")
                    continue
                
                return guess.upper()
            
            except KeyboardInterrupt:
                print("\nGame interrupted. Goodbye!")
                return 'quit'
    
    def play_game(self):
        """Main game loop."""
        print("Welcome to Hangman Game!")
        print("Guess the word one letter at a time.")
        print("You have 6 incorrect guesses before the game ends.")
        input("\nPress Enter to start...")
        
        while not self.game_over:
            self.display_game_state()
            
            guess = self.get_player_guess()
            
            if guess == 'quit':
                print("\nThanks for playing! Goodbye!")
                return
            
            valid_guess = self.make_guess(guess)
            
            if valid_guess:
                input("\nPress Enter to continue...")
        
        # Game over - display final result
        self.display_game_state()
        
        if self.won:
            print("\n🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the word '{self.word}' correctly!")
            print(f"You won with {self.max_incorrect_guesses - self.incorrect_guesses} guesses remaining!")
        else:
            print("\n💀 GAME OVER 💀")
            print(f"The word was: '{self.word}'")
            print("Better luck next time!")
    
    def play_again(self):
        """Ask if player wants to play again."""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")


def main():
    """Main function to run the Hangman game."""
    game = HangmanGame()
    
    print("🎮 Welcome to CodeAlpha Hangman Game! 🎮")
    print("=" * 50)
    
    while True:
        game.reset_game()
        game.play_game()
        
        if not game.play_again():
            print("\nThank you for playing CodeAlpha Hangman Game!")
            print("Happy coding! 🐍")
            break


if __name__ == "__main__":
    main()