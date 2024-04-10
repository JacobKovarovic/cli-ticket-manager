import os
import sys
import pytest
from src.cli_ticket_manager.classes.queue import Queue, PriorityQueue
from src.cli_ticket_manager.classes.task import Task

@pytest.fixture
def q():
    q = Queue()
    # Add some items to the queue
    q.enqueue("Item 1")
    q.enqueue("Item 2")
    q.enqueue("Item 3")
    return q

@pytest.fixture
def task1():
    return Task(
        description="Task 1",
        team="programming",
        leadDays=5,
        priority=2,
        dateCreated="2023, 04, 01",
        claimedBy="Jim",
        finished=False
    )

@pytest.fixture
def task2():
    return Task(
        description="Task 2",
        team="art",
        leadDays=5,
        priority=1,
        dateCreated="2023, 04, 02",
        claimedBy="Jim",
        finished=False
    )

@pytest.fixture
def task3():
    return Task(
        description="Task 3",
        team="sound",
        leadDays=5,
        priority=3,
        dateCreated="2023, 04, 03",
        claimedBy="Jim",
        finished=False
    )

@pytest.fixture
def pq(task1,task2,task3):
    pq = PriorityQueue()
    # Add some items to the queue
    pq.enqueue(task1)
    pq.enqueue(task2)
    pq.enqueue(task3)
    return pq

"""
Abstract Queue Tests
"""
#Init test
def test_abstract_queue_init():
    # Initialize a Queue instance
    queue = Queue()
    
    # Assert that the queue is initialized with an empty list or similar structure
    assert queue.isEmpty(), "Expected the queue to be initialized with an empty list"

#To string test
def test_abstract_queue_str(q):
    
    #Define the expected string representation
    expected_str = "\nItem 1\nItem 2\nItem 3\n"
    
    #Get the string representation of the queue
    queue_str = str(q)
    
    # Assert that the string representation matches the expected output
    assert queue_str == expected_str, f"Expected:\n{expected_str}\nGot:\n{queue_str}"

#repr (JSON) to string
def test_abstract_queue_repr(q):
    # Define the expected machine-readable representation
    expected_repr = "['Item 1', 'Item 2', 'Item 3']"
    
    # Get the machine-readable representation of the queue
    queue_repr = repr(q)
    
    # Assert that the machine-readable representation matches the expected output
    assert queue_repr == expected_repr, f"Expected:\n{expected_repr}\nGot:\n{queue_repr}"

#Iterable function
def test_abstract_queue_iter(q):
    # Define the expected order of items
    expected_items = ["Item 1", "Item 2", "Item 3"]
    
    # Iterate over the queue and collect the items
    actual_items = [item for item in q]
    
    # Assert that the items are returned in the correct order
    assert actual_items == expected_items, f"Expected: {expected_items}\nGot: {actual_items}"

#Is Empty Test
def test_abstract_queue_isEmpty(q):
    is_empty = q.isEmpty()
    assert not is_empty
    #Empty Queue
    q.dequeue()
    q.dequeue()
    q.dequeue()
    is_empty = q.isEmpty()
    assert is_empty

"""
Queue Tests
"""
#Clone Test
def test_queue_clone(q):
    # Clone the original queue
    cloned_queue = q.clone()
    
    # Assert that the cloned queue is a separate instance
    assert q is not cloned_queue, "Expected the cloned queue to be a separate instance"
    
    # Assert that the cloned queue has the same items as the original queue
    assert list(q) == list(cloned_queue), "Expected the cloned queue to have the same items as the original queue"

#Enqueue Test
def test_queue_enqueue():
    # Initialize a Queue instance
    queue = Queue()
    
    # Add an item to the queue
    queue.enqueue("Item 1")
    
    # Assert that the item was added to the queue
    assert list(queue)[0] == "Item 1", "Expected the item to be added to the queue"
#Dequeue Test
def test_queue_dequeue(q):
    # Remove Item 1 from the queue
    q.dequeue()
    
    # Assert that the item was added to the queue
    assert list(q)[0] == "Item 2", "Expected Item 1 to be removed from the queue"

#Peek Test
def test_queue_peek(q):
    # Peek at the first item in the queue
    first_item = q.peek()
    
    # Assert that the first item is "Item 1"
    assert first_item == "Item 1", "Expected the first item to be 'Item 1'"
    
    # Assert that the queue has not been modified
    assert list(q) == ["Item 1", "Item 2", "Item 3"], "Expected the queue to remain unchanged"

"""
Priority Queue Tests
"""
#Clone Test
def test_priority_queue_clone(pq):
    # Clone the original priority queue
    cloned_priority_queue = pq.clone()
    
    # Assert that the cloned priority queue is a separate instance
    assert pq is not cloned_priority_queue, "Expected the cloned priority queue to be a separate instance"
    
    # Assert that the cloned priority queue has the same items as the original priority queue
    assert list(pq) == list(cloned_priority_queue), "Expected the cloned priority queue to have the same items as the original priority queue"

#Enqueue Test
def test_priority_queue_enqueue(task1,task2):
    # Initialize a PriorityQueue instance
    pq = PriorityQueue()

    #Task 1 priority: 2 
    #Task 2 priority: 1 
    pq.enqueue(task2)
    
    # Assert that the item was added to the queue with the correct priority
    assert pq.peek() == task2, "Expected to see task2 at root of heap"    

    # Add another item with a higher priority
    pq.enqueue(task1)
    
    # Assert that the item with the higher priority is now at the front of the queue
    assert pq.peek() == task2, "Expected the item with the higher priority to be at the front of the queue"

#Dequeue Test
def test_priority_queue_dequeue(pq, task1, task2):
    #Dequeue highest priority item (should be task2)
    dequeued_task = pq.dequeue() 

    # Assert that the item was added to the queue with the correct priority
    assert dequeued_task == task2, "Expected to see task2 dequeued for highest priority"    

    #Top of queue should be task1 with a priority of 2
    assert pq.peek() == task1, "Expected to see task1 at top of Priority Queue"

#Peek Test
def test_priority_queue_peek(pq,task1,task2,task3):
    # Peek at the item with the highest priority in the queue
    highest_priority_task = pq.peek()
    
    # Assert that the item with the highest priority is "Item 3"
    assert highest_priority_task == task2, "Expected the item with the highest priority to be 'Item 3'"
    
    # Assert that the queue has not been modified by the peek operation
    assert list(pq) == [task2,task1,task3], "Expected the queue to remain unchanged"