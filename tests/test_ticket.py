import os
import sys
import pytest
sys.path.insert(1, os.path.join(sys.path[0], '..')) 
from src.utils.task import Task
from src.utils.ticket import Ticket

@pytest.fixture
def ticket1():
    task1 = Task("Task1", "art", 3, 1)
    task2 = Task("Task2", "programming", 3, 2)
    tasks = [task1, task2]
    ticket = Ticket("Ticket01","Jacob's Ticket",tasks,3,5)
    return ticket

@pytest.fixture
def ticket2():
    task1 = Task("Task1", "sound", 4, 1)
    task2 = Task("Task2", "management", 3, 2)
    tasks = [task1, task2]
    ticket = Ticket("Ticket02","Sam's Ticket",tasks,2,7)
    return ticket

@pytest.fixture
def expected_list(ticket1):
    date = ticket1.creationDate.strftime("%Y, %m, %d")
    tasks = [task.toList() for task in ticket1.tasks]
    return ["Ticket01","Jacob's Ticket",tasks,3,5,date,False]

#Testing lesser than
def test_lt_operator(ticket2,ticket1):
    
    # Use the < operator to compare the tickets
    result = ticket2 < ticket1
    
    # Assert that the comparison result is True
    assert result, "Expected ticket2 to have a lower priority than ticket1"

#Testing greater than
def test_gt_operator(ticket1,ticket2):
    
    # Use the < operator to compare the tasks
    result = ticket1 > ticket2
    
    # Assert that the comparison result is True
    assert result, "Expected ticket1 to have a higher priority than ticket2"
    
#Equal Test
def test_eq_operator(ticket1,ticket2):
    
    # Use the == operator to compare the tickets
    result = ticket1 == ticket2
    
    # Assert that the comparison result is False
    assert result==False, "Expected ticket1 to not equal ticket2"

#To string test
def test_str_operator(ticket1):
    
    # Call the __str__ method
    ticket_str = str(ticket1)
    tasks = "" 
    for task in ticket1.tasks:
        tasks += str(task) + "\n"
    # Define the expected string representation
    expected_str = f"Ticket: Ticket01\nJacob's Ticket\nDue Date: {ticket1.dueDate}\nPriority: 3\nClosed: No\n===================================\n{tasks}"
    
    # Assert that the returned string matches the expected format
    assert ticket_str == expected_str, f"Expected:\n{expected_str}\nGot:\n{ticket_str}"

def test_toList(ticket1,expected_list):
    
    # Call the toList method
    ticket_list = ticket1.toList()
    
    # Assert that the output matches the expected output
    assert ticket_list == expected_list, f"Expected {expected_list}, but got {ticket_list}"

#TODO: _updateCompletionStatus

#getTitle
def test_getTitle(ticket1):
    # Call the getTitle method
    title = ticket1.getTitle()
    
    # Assert that the output matches the expected title
    assert title == "Ticket01", f"Expected title to be 'Ticket01', but got {title}"

#getNextTask
def test_getNextTask(ticket1):
    # Call the getNextTask method
    task = ticket1.getNextTask()
    task1 = Task("Task1", "art", 3, 1)
    # Assert that the output matches the expected title
    assert task == task1, f"Expected task to be equal to task1, but got {task}"
