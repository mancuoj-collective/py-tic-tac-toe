from dataclasses import dataclass

from .players import Player
from .renderers import Renderer


@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    renderer: Renderer
