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

        for i in range(len(word)):
            if word[i] in curr_node.children: 
                curr_node = curr_node.children[word[i]]
            
            else:
                curr_node.children[word[i]] = _Node()
                curr_node = curr_node.children[word[i]]
            
            if i == (len(word) - 1) and not curr_node.is_word:
                curr_node.is_word = True
                self._size += 1
            
    def __contains__(self, word: str) -> bool:
        curr_node = self._root

        for i in range(len(word)):
            if word[i] in curr_node.children: 
                curr_node = curr_node.children[word[i]]
                
                if i == (len(word) - 1) and curr_node.is_word:
                    return True
            else: 
                return False   
        return False

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[str]:
        return self.__iter__helper(self._root, "", "");

    def __iter__helper(self, node, word, last_letter):
        word += last_letter

        if len(node.children) == 0:
            return 

        else:
            for child in node.children:
                if node.children[child].is_word: 
                    yield word + child
                yield from self.__iter__helper(node.children[child], word, child)


    def starts_with(self, prefix: str) -> list[str]:
        """Return all words beginning with `prefix`."""
        raise NotImplementedError
