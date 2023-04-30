from heaps import MinHeap, _AbstractHeap

myheap = MinHeap()
abstractHeap = _AbstractHeap
for i in range(4):
    myheap.push(i)
print(myheap)