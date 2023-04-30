from heaps import MinHeap

myheap = MinHeap()
for i in range(4):
    myheap.push(i)
print(myheap)
myheapClone = myheap.clone()
print(myheap)
print(myheapClone)
print(type(myheapClone))
myheapClone.clear()
print(myheap)
print(myheapClone)