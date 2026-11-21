import pytest
from spellbook.heap import Heap

def test_len_peek():
    h = Heap()
    h._items.append(1)
    h._items.append(2)

    assert len(h) == 2
    assert h.peek() == 1

def test_len_peek_empty_h():
    h = Heap()
    assert len(h) == 0
    with pytest.raises(IndexError):
        h.peek()

def test_pushing_p():
    h = Heap()
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1) 
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1)

    assert len(h) == 21
    assert h.peek() == 1


def test_popping_p():
    h = Heap()
    h.push(19)
    h.push(12)
    h.push(1)
    h.push(19)
    h.push(12)
    h.push(1) 
    h.push(19)
    h.push(12)

    
    popped = h.pop()
    assert popped == 1

    popped = h.pop()
    assert popped == 1

    popped = h.pop()
    assert popped == 12
