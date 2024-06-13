from dataclasses import dataclass
from functools import cached_property

from .grid import Grid
from .mark import Mark


@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark.CROSS

    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other
