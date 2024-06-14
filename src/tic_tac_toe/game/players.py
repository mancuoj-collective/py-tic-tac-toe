from abc import ABC, abstractmethod

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.models.game_state import GameState
from tic_tac_toe.models.mark import Mark
from tic_tac_toe.models.move import Move


class Player(ABC):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other player's turn")

    @abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""
