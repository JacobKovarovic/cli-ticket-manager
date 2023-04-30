# Set path for module imports from parent directory
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

from src.heaps import MinHeap, _AbstractHeap

myheap = MinHeap()
abstractHeap = _AbstractHeap
for i in range(4):
    myheap.push(i)
print(myheap)