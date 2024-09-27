'''My Calculator Test'''
import pytest
from app.operations import addition, division, multiplication, subtraction

def test_addition():
    '''Addition function's'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''subtraction function'''
    assert subtraction(1,1) == 0

def test_mulitplication():
    '''multiplication function'''
    assert multiplication(1,2) == 2

def test_positive_division():
    '''Positive Division function'''
    assert division(2,2) == 1

def test_division_by_zero_exception():
    '''Division Function testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)
