from spellbook.trie import Trie

# contain and len
def test_empty_trie():
    t = Trie()
    assert len(t) == 0
    assert "a" not in t

# insert and contain
def test_insert_and_contains():
    t = Trie()
    t.insert("cat")
    t.insert("cats")
    assert "cat" in t
    assert "ca" not in t
    assert "cats" in t

# insert and len
def test_insert_duplicate():
    t = Trie()
    t.insert("dod")
    t.insert("dod")
    assert len(t) == 1

# insert and len
def test_len_func():
    t = Trie()
    t.insert("Sleep")
    t.insert("Turn")
    t.insert("Sleepy")
    t.insert("Relax")
    t.insert("Val")
    assert len(t) == 5

# insert and contain
def test_not_contains():
    t = Trie()
    t.insert("Human")
    assert "Huxman" not in t

# insert and contain
def test_contains_with_same_letters():
    t = Trie()
    t.insert("doubled")
    assert "d" not in t

# iter and contain
def test_iter_trie():
    t = Trie()
    l = list()
    l.append("Ban")
    l.append("Won")
    l.append("Wom")
    l.append("Bann")

    t.insert("Ban")
    t.insert("Won")
    t.insert("Wom")
    t.insert("Bann")
    for word in t:
        print(word)
        assert word in l
        assert word in t

# iter and contain
def test_iter_empty_trie():
    t = Trie()
    counter = 0
    for _ in t:
        counter += 1
    assert counter == 0
