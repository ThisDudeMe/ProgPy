import pytest
from app.math import multiply, add


#naming is IMPORTANT!!!!! function and file that is testing always must start with "test_"
def test_add():

    #ARRANGE

    num1 = 10
    num2 = 20

    #ACT

    sum = add(num1, num2)

    #ASSERT

    assert sum == 30

def test_multiply():

    #ARRANGE

    num1 = 5
    num2 = 10

    #ACT

    sum = multiply(num1, num2)
    #ASSERT

    assert sum == 40

def testnotexecuted():
    assert 10 == 10