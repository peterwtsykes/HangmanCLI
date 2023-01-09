import sys
from dataclasses import dataclass
from Exceptions import InvalidWordError, InvalidLetterError, AlreadyGuessedError, MultipleLettersError

@dataclass
class Letter:
    letter: str
    known: bool


class HangmanGame:
    def __init__(self):
        #should num_wrong_guesses be in HangmanCLI?
        #self._num_wrong_guesses = 0
        self.word = None
        self._word_array = []
        self._guessed_letters = []

    def update_word(self, word):
        if not word.isalpha():
            raise InvalidWordError
        else:
            self.word = word.upper()
            for i in range(len(word)):
                self._word_array.append(Letter(self.word[i], False))

    def print_word(self):
        for i in range(len(self.word)):
            if self._word_array[i].known:
                print(self._word_array[i].letter, end=" ")
            else:
                print("_", end=" ")
        print("\n")

    def check_won(self):
        won = True
        for i in range(len(self.word)):
            if not self._word_array[i].known:
                won = False
                break
        return won
    
    def check_valid_letter(self, letter):
        if not letter.isalpha():
            raise InvalidLetterError
        if letter in self._guessed_letters:
            raise AlreadyGuessedError
        if len(letter) > 1:
            raise MultipleLettersError

    def test_in_word(self, letter):
        num_occurrences = 0
        for i in range(len(self.word)):
            if self._word_array[i].letter == letter:
                self._word_array[i].known = True
                num_occurrences += 1
        self._guessed_letters.append(letter)
        return num_occurrences
