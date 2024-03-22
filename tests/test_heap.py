import pytest
from src.utils.heap import MinHeap

@pytest.fixture
def myheap():
    heap = MinHeap()
    for i in range(4):
        heap.push(i)
    return heap


def test_heap(myheap):
    for i in range(4):
        item = myheap.pop()
        assert item == i
