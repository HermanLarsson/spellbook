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
        curr_node = self._root

        for ch in word:
            if ch in curr_node.children: 
                curr_node = curr_node.children[ch]
            
            else:
                curr_node.children[ch] = _Node()
                curr_node = curr_node.children[ch]
                if ch == word[-1]:
                    curr_node.is_word = True
            
    def __contains__(self, word: str) -> bool:
        curr_node = self._root

        for ch in word:
            if ch in curr_node.children: 
                curr_node = curr_node.children[ch]
                
                if ch == word[-1] and curr_node.is_word:
                    return True

        return False
            
    def __len__(self) -> int:
        """Enables `len(trie)`: the number of distinct words."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        """Enables `for word in trie`. Yield every word (hint: recursion + `yield from`)."""
        raise NotImplementedError

    def starts_with(self, prefix: str) -> list[str]:
        """Return all words beginning with `prefix`."""
        raise NotImplementedError
