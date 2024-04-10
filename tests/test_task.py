import pytest
import os
import sys
from datetime import date, timedelta, datetime
from src.cli_ticket_manager.classes.task import Task

@pytest.fixture
def task1():
    return Task("MyTask", "art", 3, 1)

@pytest.fixture
def task2():
    return Task("MyTask2", "programming", 3, 2)

@pytest.fixture
def task3():
    return Task(
        description="Implement scroll feature",
        team="programming",
        leadDays=5,
        priority=3,
        dateCreated="2023, 04, 01",
        claimedBy="Jim",
        finished=False
    )

@pytest.fixture
def expected_list_output():
    return [
        "Implement scroll feature",
        "programming",
        5,
        3,
        "2023, 04, 01",
        "Jim",
        False
    ]

#Test Task constructor by adding an invalid team
def test_Task():
    #Incorrect constructor args should raise ValueError 
    with pytest.raises(ValueError) as err:
        task = Task("New", "Wrong Team", 3, 3)
    assert err.type is ValueError
         
#Testing lesser than
def test_lt_operator(task1,task2):
    
    # Use the < operator to compare the tasks
    result = task1 < task2
    
    # Assert that the comparison result is True
    assert result, "Expected task1 to have a lower priority than task2"

#Testing greater than
def test_gt_operator(task2,task1):
    
    # Use the < operator to compare the tasks
    result = task2 > task1
    
    # Assert that the comparison result is True
    assert result, "Expected task2 to have a higher priority than task1"
    
#Equal Test
def test_eq_operator(task1,task2):
    
    # Use the == operator to compare the tasks
    result = task1 == task2
    
    # Assert that the comparison result is False
    assert result==False, "Expected task1 to not equal task2"

#To string test
def test_str_operator(task1):
    
    # Call the __str__ method
    task_str = str(task1)
    
    # Define the expected string representation
    expected_str = f"Task: MyTask\nTeam: art\nDue Date: {task1.dueDate}\nPriority: 1\nComplete: No\nClaimed By: None\n"
    
    # Assert that the returned string matches the expected format
    assert task_str == expected_str, f"Expected:\n{expected_str}\nGot:\n{task_str}"

def test_toList(task3,expected_list_output):
    
    # Call the toList method
    task_list = task3.toList()
    
    # Assert that the output matches the expected output
    assert task_list == expected_list_output, f"Expected {expected_list_output}, but got {task_list}"


# Test function using the fixture
def test_daysTilDue(task3):
    # Calculate the expected number of days until the task is due
    # by adding the leadDays to the current date.
    expected_days = (date.today() - task3.dueDate).days
    print(expected_days) 
    # Call the daysTilDue method
    days_til_due = task3.daysTilDue()
    
    # Assert that the output matches the expected number of days
    assert days_til_due == expected_days, f"Expected {expected_days}, but got {days_til_due}"

# Test function using the fixture
def test_getLeadDays(task3):
    # Call the getLeadDays method
    lead_days = task3.getLeadDays()
    
    # Assert that the output matches the expected leadDays
    assert lead_days == 5, f"Expected leadDays to be 5, but got {lead_days}"

def test_getTeam(task3):
    # Call the getTeam method
    team = task3.getTeam()
    
    # Assert that the output matches the expected team
    assert team == "programming", f"Expected team to be 'programming', but got {team}"

def test_ParentTicket(task2,task3):
    # Call the setParent method
    task3.setParentTicket(task2)
    
    parent = task3.getParentTicket()
    # Assert that the output matches the expected parentTicket
    assert parent == task2, f"Expected parent to be 'task2', but got {parent}"

def test_Owner(task3):
    # Call the setOwner method to change from Jim to Maria
    task3.setOwner("Maria")
    
    owner = task3.getOwner()
    # Assert that the output matches the expected Owner
    assert owner == "Maria", f"Expected owner to be 'Maria', but got {owner}"

def test_isFinished(task3):
    # Call the isFinished method
    fin = task3.isFinished()
    
    #Expect to recieve false
    assert fin == False, f"Expected false, but got {fin}"

    #Test finishTask Method
    task3.finishTask()
    fin = task3.isFinished()
    assert fin == True, f"Expected True, but got {fin}"