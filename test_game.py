import pytest
import mastermind.mastermind_core as mastermind


def test_check_guess():
    state = mastermind.GameState([1, 2, 3, 4], 5, 10)

    result = state.check_guess([1, 2, 3, 4])
    assert result == mastermind.GuessResult(
        full_correct=4, correct_color=0, game_status=None
    )

    result = state.check_guess([5, 5, 5, 4])
    assert result == mastermind.GuessResult(
        full_correct=1, correct_color=0, game_status=None
    )

    result = state.check_guess([2, 5, 5, 5])
    assert result == mastermind.GuessResult(
        full_correct=0, correct_color=1, game_status=None
    )

    result = state.check_guess([4, 2, 6, 6])
    assert result == mastermind.GuessResult(
        full_correct=1, correct_color=1, game_status=None
    )

    with pytest.raises(ValueError):
        state.check_guess([1])