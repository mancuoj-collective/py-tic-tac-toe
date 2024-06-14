from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.game.players import Player
    from tic_tac_toe.models.game_state import GameState
    from tic_tac_toe.models.grid import Grid
    from tic_tac_toe.models.mark import Mark

from .exceptions import InvalidGameState


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)


def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")


def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    if grid.x_count > grid.o_count:
        if starting_mark != Mark.CROSS:
            raise InvalidGameState("Wrong starting mark")
    elif grid.o_count > grid.x_count:
        if starting_mark != Mark.NAUGHT:
            raise InvalidGameState("Wrong starting mark")


def validate_winner(grid: Grid, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == Mark.CROSS:
        if starting_mark == Mark.CROSS:
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
    elif winner == Mark.NAUGHT:
        if starting_mark == Mark.NAUGHT:
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong number of Os")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Wrong number of Os")


def validate_players(player1: Player, player2: Player) -> None:
    if player1.mark is player2.mark:
        raise ValueError("Players must use different marks")
