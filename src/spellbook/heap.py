"""Milestone 2: a binary min-heap, written from scratch.

Your task: implement the Heap class below. Delete each `raise NotImplementedError`
as you go, and write tests in tests/test_heap.py to check your progress.
"""

#parent(i) = (i - 1) // 2
#left_child(i)   = 2*i + 1
#right_child(i)  = 2*i + 2



class Heap[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def _parent(self, i):
        p_idx = (i - 1) // 2
        if p_idx < 0:
            return i
        return p_idx
    
    def _left_child(self, i):
        return 2 * i + 1
    
    def _right_child(self, i):
        return 2 * i + 2
    
    def push(self, item: T) -> None:
        self._items.append(item)
        self._swim(len(self._items) - 1)
        

    def pop(self) -> T:
        if len(self._items) == 0:
            raise IndexError("Heap is empty")
        
        popped = self._items[0]
        self._items[0] = self._items[-1]
        self._sink(0)
        return popped


    def peek(self) -> T:
        if len(self._items) == 0:
            raise IndexError("Heap is empty")
        
        return self._items[0]

    def __len__(self) -> int:
        return len(self._items)

    def _swim(self, i):
        swimmer = self._items[i]
        parent_idx = self._parent(i)
        parent = self._items[parent_idx]
        
        while parent > swimmer:
            self._items[i] = parent
            self._items[parent_idx] = swimmer     
            i = parent_idx        

            parent_idx = self._parent(i)
            parent = self._items[parent_idx]

    def _sink(self, i):
        sinker = self._items[i]

        left_child_idx = self._left_child(i)
        right_child_idx = self._right_child(i)
        if left_child_idx < len(self._items):
            left_child = self._items[left_child_idx]
        if right_child_idx < len(self._items):
            right_child = self._items[right_child_idx]

        while (sinker > left_child or sinker > right_child) and (left_child_idx < len(self._items) or right_child_idx < len(self._items)):

            if left_child < right_child:
                self._items[i] = left_child
                self._items[left_child_idx] = sinker
                i = left_child_idx
            else: 
                self._items[i] = right_child
                self._items[right_child_idx] = sinker
                i = right_child_idx

        left_child_idx = self._left_child(i)
        right_child_idx = self._right_child(i)
        if left_child_idx < len(self._items):
            left_child = self._items[left_child_idx]
        if right_child_idx < len(self._items):
            right_child = self._items[right_child_idx]
