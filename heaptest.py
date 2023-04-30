from heaps import MinHeap

myheap = MinHeap()
for i in range(20):
    myheap.push(i)
print(myheap)
myheap.printLikeTree()