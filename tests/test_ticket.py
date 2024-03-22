import os
import sys
import pytest
from datetime import date, timedelta
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
def ticket3():
    task1 = Task("Task1", "programming", 2, 1)
    task2 = Task("Task2", "management", 3, 2)
    tasks = [task1, task2]
    ticket = Ticket("Ticket03","Tina's Ticket",tasks,2,leadDays=5)
    return ticket

@pytest.fixture
def due_date():
    return date.today() + timedelta(days=5)

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

#Test the finished task methods
def test_finishTasks(ticket2):
    #test unfinishedTasks method
    unfinished_tasks = ticket2.getUnfinishedTasks()
    task1 = Task("Task1", "sound", 4, 1)
    task2 = Task("Task2", "management", 3, 2)
    tasks = [task1, task2]
    assert unfinished_tasks == tasks

    #Finish task1
    ticket2.finishNextTask()
    task1.finishTask()
    finish_t = [task1]

    #Test getFinishedTasks method
    finished_tasks = ticket2.getFinishedTasks()
    assert finished_tasks == finish_t,f"Expected {finish_t}, but got {finished_tasks}"

def test_daysTilDue(ticket3):
    #For ticket 3 the leadDays = 5
    days_til_due = ticket3.daysTilDue()
    
    # Assert that the returned value matches the expected number of days until the due date
    assert days_til_due == 5, f"Expected 5 days until due, but got {days_til_due}" 

def test_Closed(ticket2):
    #Checking ticket status
    status = ticket2.isClosed()
    assert status == False, f"Expected ticket to be open, but getting {status}"
    #Closing ticket and checking status
    ticket2.close()
    status = ticket2.isClosed()
    assert status, f"Expected ticket to be closed, but getting {status}"
