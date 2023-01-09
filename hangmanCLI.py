import sys
import os
from dataclasses import dataclass
from hangmanGame import HangmanGame
from Exceptions import InvalidWordError, InvalidLetterError, AlreadyGuessedError, MultipleLettersError

class HangmanCLI:
    def __init__(self):
        self._game = HangmanGame()
        self._num_wrong_guesses = 0
    
    def run(self):
        #Enter word you would like player to guess
        word = input("Please enter a word: ")
        valid_word = False
        while not valid_word:
            try:
                self._game.update_word(word)
                valid_word = True
            except InvalidWordError:
                word = input("Please try again: ")
        #Clear terminal so player can't see word
        os.system('clear')
        print("\nLET'S PLAY HANGMAN\n")
        #Gameplay
        while self._num_wrong_guesses < 6:
            self._print_board()
            self._print_word()
            #Check if already won
            if self._game.check_won():
                print("You won :)\n")
                sys.exit()
            letter = input("Please guess a letter: ")
            #Check if valid letter
            valid_letter = False
            while not valid_letter :
                try:
                    self._game.check_valid_letter(letter.upper())
                except InvalidLetterError:
                    letter = input("That's not a letter. Please try again: ")
                except AlreadyGuessedError:
                    letter = input(f"You already guessed {letter.upper()}. Please try again: ")
                except MultipleLettersError:
                    letter = input("Please only guess one letter: ")
                else:
                    valid_letter = True
            #Test to see if letter is in word
            upper_letter = letter.upper()
            num_occurrences = self._game.test_in_word(upper_letter)
            if num_occurrences == 0:
                self._num_wrong_guesses += 1
            if num_occurrences == 1:
                print(f"\nThere is 1 {upper_letter}\n")
            else:
                print(f"\nThere are {num_occurrences} {upper_letter}s\n")
        #Print you lost
        self._print_board()
        self._print_word()
        print(f"You lost :(\nThe word was {self._game.word}\n")

    def _print_board(self):
        #Top row
        print(" |------|")
        #Second row (head)
        if self._num_wrong_guesses == 0:
            print(" |")
        else:
            print(" |      0")
        #Third row (torso/arms)
        if self._num_wrong_guesses < 2:
            print(" |")
        elif self._num_wrong_guesses == 2:
            print(" |      |")
        elif self._num_wrong_guesses == 3:
            print(" |     -|")
        else:
            print(" |     -|-")
        #Fourth row (waist)
        if self._num_wrong_guesses < 2:
            print(" |")
        else:
            print(" |      |")
        #Fifth row (legs)
        if self._num_wrong_guesses < 5:
            print(" |")
        elif self._num_wrong_guesses == 5:
            print(" |     /")
        else:
            print(" |     / \ ")
        #bottom
        print(""" |
------------""")

    def _print_word(self):
        self._game.print_word()
    
if __name__ == "__main__":
    HangmanCLI().run()
