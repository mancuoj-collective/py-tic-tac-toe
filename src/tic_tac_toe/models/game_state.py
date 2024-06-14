import re
from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.validators import validate_game_state

from .grid import Grid
from .mark import Mark
from .move import Move

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)


@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark.CROSS

    def __post_init__(self) -> None:
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_cells == 9

    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None

    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def winner(self) -> Mark:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [match.start() for match in re.finditer(r"\?", pattern)]
        return []

    def make_move_to(self, index: int) -> Move:
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1 :]
                ),
                self.starting_mark,
            ),
        )

    @cached_property
    def possible_moves(self) -> list[int]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves
