import os
import sys
# Set path for module imports from parent directory
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

def main():
    from src.heaps import MinHeap, _AbstractHeap

    myheap = MinHeap()
    abstractHeap = _AbstractHeap
    for i in range(4):
        myheap.push(i)
    print(myheap)

if __name__ == "__main__":
    main()