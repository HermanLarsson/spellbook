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
    assert "ca" not in t
    assert "cats" in t

def test_insert_duplicate():
    t = Trie()
    t.insert("dod")
    t.insert("dod")
    assert len(t) == 1

def test_len_func():
    t = Trie()
    t.insert("Sleep")
    t.insert("Turn")
    t.insert("Sleepy")
    t.insert("Relax")
    t.insert("Val")
    assert len(t) == 5

def test_not_contains():
    t = Trie()
    t.insert("Human")
    assert "Huxman" not in t

def test_contains_with_same_letters():
    t = Trie()
    t.insert("doubled")
    assert "d" not in t