from spellbook.trie import Trie


def test_empty_trie():
    t = Trie()
    assert len(t) == 0
    assert "a" not in t


def test_insert_and_contains():
    t = Trie()
    t.insert("cat")
    assert "cat" in t
    assert "ca" not in t  # a prefix is not a word


# TODO (you): add tests for duplicates, __iter__, starts_with,
# the empty-string prefix, and a prefix that matches nothing.
