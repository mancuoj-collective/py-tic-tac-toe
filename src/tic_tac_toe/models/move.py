from dataclasses import dataclass

from .game_state import GameState
from .mark import Mark


@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: GameState
    after_state: GameState
