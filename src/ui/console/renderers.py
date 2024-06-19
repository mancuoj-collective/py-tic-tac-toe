import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState


class ConsoleRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        clear_screen()
        if game_state.winner:
            print(f"{game_state.winner.value} wins \N{PARTY POPPER}")
        else:
            print_solid(game_state.grid.cells)
            if game_state.tie:
                print("No one wins this time \N{NEUTRAL FACE}")


def clear_screen() -> None:
    print("\033c", end="")


def print_solid(cells: Iterable[str]) -> None:
    print(
        textwrap.dedent(
            """\
            A B C
           -------
        1 | {0} {1} {2} |
        2 | {3} {4} {5} |
        3 | {6} {7} {8} |
           -------
    """
        ).format(*cells)
    )
