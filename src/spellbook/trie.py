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


    def _find_node(self, prefix) -> _Node | None:
                
        curr_node = self._root

        for i in range(len(prefix)):
            if prefix[i] in curr_node.children: 
                curr_node = curr_node.children[prefix[i]]
            else: 
                return None

        return curr_node
        

    def insert(self, word: str) -> None:
        if str is not type(word) or word == "":
            return
        
        curr_node = self._root

        for i in range(len(word)):
            if word[i] in curr_node.children: 
                curr_node = curr_node.children[word[i]]
            
            else:
                curr_node.children[word[i]] = _Node()
                curr_node = curr_node.children[word[i]]
            
        if not curr_node.is_word:
            curr_node.is_word = True
            self._size += 1


    def __contains__(self, word: str) -> bool:
        curr_node = self._find_node(word)
        if curr_node and curr_node.is_word:
            return True 
        return False


    def __len__(self) -> int:
        return self._size


    def __iter__(self) -> Iterator[str]:
        return self._iter_helper(self._root, "")


    def _iter_helper(self, node, word) -> Iterator[str]: 
        for child in node.children:
            if node.children[child].is_word: 
                yield word + child
            yield from self._iter_helper(node.children[child], word + child)

        
    def starts_with(self, prefix: str) -> list[str]:
        all_words = list()
        curr_node = self._find_node(prefix)

        if not curr_node:
            return []
        
        return self._starts_with_helper(curr_node, prefix, all_words)

            
    def _starts_with_helper(self, curr_node, curr_word, all_words) -> list[str]:
        if curr_node.is_word:
            all_words.append(curr_word)

        for child in curr_node.children:
            all_words = self._starts_with_helper(curr_node.children[child], curr_word + child, all_words)

        return all_words