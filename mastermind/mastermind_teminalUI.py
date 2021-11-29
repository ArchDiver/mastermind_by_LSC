from typing import List
import sys

import logging as log
# from mastermind_core import GameStatus

import mastermind_core as game


class TerminalUI:
    def __init__(self):
        self.game = None

    def play(self):
        """
        Play the game forever, until the user asks to quit.
        """
        self.game = game.GameState.random_game(4, 8, 2)
        while True:
            print("\n\n             Welcome to Mastermind by LSC\n")
            print("To win you need to fully guess ALL of the numbers.")
            print("After each full guess you will get your guess results:")
            print("    'Fully Correct' means correct number in the correct position.")
            print(
                "    'Correct Color' means the color is correct but the position is NOT.\n")
            guess = self.get_guess()
            self.evaluate_guess(guess)

    def get_int(self, prompt: str) -> int:
        """
        Get an int from the user. Tries repeatedly until an int is entered.
        """
        while True:
            num_str = input(prompt)
            try:
                return int(num_str)
            except ValueError:
                pass

    def get_yes_no(self, prompt: str) -> bool:
        """
        As get_int, but returns a boolean. Anything that starts with "Y" or "y" is true,
        anything that starts with "N" or "n" is false,
        anything else is prompted again.
        """
        while True:
            answer = input(prompt)
            if answer[0].lower() == "n":
                return False
            if answer[0].lower() == "y":
                return True
            else:
                continue

    def print_board(self):
        """
        Display the number of guesses left and all the previous guesses.
        """
        print(f"You have {self.game.guesses_left()} guesses left.")
        if self.game.guess_history:
            print("Your previous guesses: ")
            for guess in self.game.guess_history:
                print(
                    "    ",
                    " ".join(str(x) for x in guess.guess),
                    f"fully correct={guess.result.full_correct}, right color={guess.result.correct_color}",
                )

    def get_guess(self) -> List[int]:
        guesses: List[int] = []
        self.print_board()
        while len(guesses) < self.game.num_pegs():
            peg_num = len(guesses) + 1
            prompt = f"Enter peg {peg_num} color (number) from 0 to {self.game.num_colors - 1}: "
            guess = self.get_int(prompt)
            if guess < 0 or guess >= self.game.num_colors:
                continue
            guesses.append(guess)
        print()
        return guesses

    def evaluate_guess(self, colors: List[int]):
        result = self.game.take_guess(colors)
        if result.full_correct == len(self.game.pegs):
            print("Winner! winner! Chicken dinner!")
            play_again = self.get_yes_no("Play again? ")
            if play_again:
                self.game = game.GameState.random_game(4, 8, 10)
            else:
                sys.exit(0)\

        elif result.game_status == game.GameStatus.LOST:
            print("You have lost.")
            play_again = self.get_yes_no("Play again? (y/n): ")
            if play_again:
                self.game = game.GameState.random_game(4, 8, 10)
            else:
                sys.exit(0)\


        else:
            print(
                f"Fully correct: {result.full_correct}; wrong location: {result.correct_color}"
            )


def main():
    log.basicConfig(
        filename="mastemind.log",
        level=log.DEBUG,
        format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s",
    )

    ui = TerminalUI()
    ui.play()


if __name__ == "__main__":
    main()
