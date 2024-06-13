from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.validators import validate_grid


@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self):
        validate_grid(self)

    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")

    @cached_property
    def empty_cells(self) -> int:
        return self.cells.count(" ")
