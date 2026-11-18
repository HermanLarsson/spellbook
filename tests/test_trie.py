from spellbook.trie import Trie


def test_empty_trie():
    t = Trie()
    assert len(t) == 0
    assert "a" not in t

def test_insert_and_contains():
    t = Trie()
    t.insert("cat")
    t.insert("cats")
    assert "cat" in t
    assert "ca" not in t  # a prefix is not a word
    assert "cats" in t

def test_insert_duplicate():
    t = Trie()
    t.insert("dog")
    t.insert("dog")
    assert "dog" in t
    assert len(t._root.children) == 1
    assert len(t._root.children["d"].children) == 1
    assert len(t._root.children["d"].children["o"].children) == 1

def test_len_func():
    t = Trie()
    t.insert("Sleep")
    t.insert("Turn")
    t.insert("Sleepy")
    t.insert("Relax")
    t.insert("Val")
    assert len(t) == 5