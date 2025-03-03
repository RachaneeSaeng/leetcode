import pytest
from solutions.binary_search.my_calendar import MyCalendar

def test_my_calendar():
    calendar = MyCalendar()
    
    # Test booking a new event
    assert calendar.book(10, 20) == True
    # Test booking an overlapping event
    assert calendar.book(15, 25) == False
    # Test booking a non-overlapping event
    assert calendar.book(20, 30) == True
    # Test booking an event that starts and ends within an existing event
    assert calendar.book(12, 18) == False
    # Test booking an event that ends when an existing event starts
    assert calendar.book(5, 10) == True
    # Test booking an event that starts when an existing event ends
    assert calendar.book(50, 60) == True
    # Test booking an event that starts when an existing event ends
    assert calendar.book(35, 45) == True
    # Test booking an event that starts when an existing event ends
    assert calendar.book(30, 50) == False

if __name__ == "__main__":
    pytest.main()