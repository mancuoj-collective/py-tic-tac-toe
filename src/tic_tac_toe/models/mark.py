from __future__ import annotations

from enum import StrEnum


class Mark(StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Mark:
        return Mark.CROSS if self == Mark.NAUGHT else Mark.NAUGHT
