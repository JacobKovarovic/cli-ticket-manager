import pytest
import sys
import os
from src.utils.heap import MinHeap
# Set path for module imports from parent directory
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

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
