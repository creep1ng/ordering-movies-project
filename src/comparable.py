"""This module is just for have an emulation of the "Comparable" interface.
Extracted from https://stackoverflow.com/a/65224102"""

from __future__ import annotations
from abc import abstractmethod
from typing import Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: CT, other: CT) -> bool:
        pass

    @abstractmethod
    def __le__(self: CT, other: CT) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)
