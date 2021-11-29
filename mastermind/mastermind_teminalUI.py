from typing import List
import sys

import logging as log

import mastermind_core as core


class TerminalUI:
    def __init__(self):
        self.core = None

    def play(self):
        """
        Plays the game in a loop till the user quits
        """
        self.core = core.GameState.random_game(4, 0, 8, 10)
        while True:
            guess = self.get_guess()
            self.eval_guess(guess)

    def get_int(self, prompt: str) -> int:
        """
        Gets int from user. Loops till int is entered.
        """
        while True:
            num_str = input(prompt)
            try:
                return int(num_str)
            except ValueError:
                pass

    def yes_no(self, prompt: str) -> bool:
        """
        Takes in a str and evaluates it for bool. Only accepts "y" or "n".
        """
        while True:
            answer = input(prompt)
            if not answer:
                continue
            if answer[0].lower() == "y":
                return True
            if answer[0].lower() == "n":
                return False

    def print_board(self):
        """
        Displays the board with previous guesses and remaining guesses
        """
        print(f"You have {self.core.guesses_left()} guesses left.")
        if self.core.guess_history:
            print("Your previous guesses: ")
            for guess in self.core.guess_history:
                print(
                    "  ",
                    " ".join(str(x) for x in guess.guess),
                    f"Fully Correct= {guess.result.full_correct}, Correct color= {guess.result.color_correct}",
                )

    def get_guess(self) -> List[int]:
        """
        Retrieves the guesses from the user and returns the list
        """
        guesses: List[int] = []
        self.print_board()
        while len(guesses) < self.core.num_pegs():
            peg_num = len(guesses) - 1
            prompt = f"Enter peg {peg_num} choice from {self.core.low_num} to {self.core.num_colors - 1}"
            guess = self.get_int(prompt)
            if guess < 0 or guess >= self.core.num_colors:
                continue
            guesses.append(guess)
            print()
            return guesses

    def eval_guess(self, colors: List[int]):
        result = self.core.take_guess(colors)
        if result.full_correct == len(self.core.pegs):
            print("WINNER!! Congrats.")
            play_again = self.yes_no("Play Again? (y/n): ")
            if play_again:
                self.core = core.GameState.random_game(4, 8, 10)
            else:
                sys.exit(0)
        else:
            print(
                f"Fully correct: {result.full_correct}; wrong location: {result.correct_color}"
            )


def main():
    log.basicConfig(
        filename="mastermind_LSC.log",
        level=log.log.DEBUG,
        format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s",
    )
    ui = TerminalUI()
    ui.play()


if __name__ == '__main__':
    main()
