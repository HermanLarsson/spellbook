"""Milestone 1: a prefix tree (trie) for autocomplete.

Your task: implement the Trie class below. Delete each `raise NotImplementedError`
as you go, and run `pytest` to check your progress.
"""

from collections.abc import Iterator
from dataclasses import dataclass, field


@dataclass
class _Node:
    children: dict[str, "_Node"] = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self._root = _Node()
        self._size = 0

    def insert(self, word: str) -> None:
        """Add a word. Inserting the same word twice should not change len()."""
        raise NotImplementedError

    def __contains__(self, word: str) -> bool:
        """Enables `"cat" in trie`. True only for whole words, not prefixes."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Enables `len(trie)`: the number of distinct words."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        """Enables `for word in trie`. Yield every word (hint: recursion + `yield from`)."""
        raise NotImplementedError

    def starts_with(self, prefix: str) -> list[str]:
        """Return all words beginning with `prefix`."""
        raise NotImplementedError
