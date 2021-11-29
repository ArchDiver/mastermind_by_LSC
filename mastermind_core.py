from typing import NamedTuple, Tuple, Dict, List, Optional
from enum import Enum

import requests
import sys

import logging as log


class Random_Num:
    def __inti__(self):
        pass

    def generate(self, low, high, max):
        """
        Generates the random numbers based on the response request.
        Takes 4 arguments:
        self, low: int, high:int, max:int
        """
        url, params = self.api_request(high, low, max)
        response = requests.get(url, params=params)
        response.raise_for_status()
        resp_txt = response.text.strip().split("\n")
        return [int(x) for x in resp_txt]

    def api_request(self, low: int, high: int, num: int) -> Tuple[str, Dict]:
        """
        Constructs the URL from the passed in values.
        Returns tuple of (URL, request_parameters)
        4 args:
        self, low:int, high:int, num:int
        """
        return (
            f"https://www.random.org/integers/",
            {
                "num": num,
                "min": low,
                "max": high,
                "base": 10,
                "col": 1,
                "format": "plain",
                "rnd": "new",
            },
        )


class GameStatus(Enum):
    PLAYING = 0
    WON = 1
    LOST = 2


class GuessResult(NamedTuple):
    full_correct: int
    color_correct: int


class GuessHistory(NamedTuple):
    guess: List[int]
    result: GuessResult


class GameState:
    def __init__(self, pegs: List[int], num_colors: int, max_guesses: int):
        self.pegs = pegs
        self.num_colors = num_colors
        self.max_guesses = max_guesses
        self.guess_history: List[GuessHistory] = []

    def num_pegs(self) -> int:
        """
        The number of pegs that the player is guessing. Avoids accessing self.pegs
        """
        return len(self.pegs)

    def check_guess(self, guess: List[int]) -> GuessResult:
        """
        Takes guess and evaluates it for correctness and returns a GuessResult.
        Fails if the number of options in the guess is not correct.

        *Does not advance game state. Merely performs check pegs.
        """
        if len(guess) != len(self.pegs):
            # Missing guesses
            raise ValueError(f"A guess requires {len(self.pegs)} items.")
        full_correct2 = 0
        correct_color2 = 0
        for i in range(len(guess)):
            if guess[i] == self.pegs[i]:
                full_correct2 += 1
            elif guess[i] in self.pegs:
                correct_color2 += 1
        return GuessResult(
            full_correct=full_correct2, correct_color=correct_color2, game_status=None
        )

    def take_guess(self, guess: List[int]) -> GuessResult:
        """
        Takes in guesses from the user and advances the GameState
        """
        result = self.check_guess(guess)
        self.guess_history.append(GuessHistory(guess=guess, result=result))

        status = GameStatus.PLAYING
        if result.full_correct == len(self.pegs):
            status = GameStatus.WON
        if self.out_of_guesses():
            status = GameStatue.LOST

        return result._replace(game_status=status)

    def out_of_guesses(self) -> bool:
        return self.guesses_left() == 0

    def guesses_left(self) -> int:
        return self.max_guesses - len(self.guess_history)

    @staticmethod
    def random_game(num_pegs: int, num_colors: int, max_guesses: int) -> "GameState":
        pegs = Random_Num().generate(low=0, high=num_colors-1, num=num_pegs)
        return GameState(pegs, num_colors, max_guesses)