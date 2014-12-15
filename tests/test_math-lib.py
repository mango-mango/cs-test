import sys

sys.path.append('../')
from mango_lib import math_lib

def test_add_numbers():
    assert math_lib.add_numbers(4, 3) == 7 

def test_mul_numbers():
    assert math_lib.mul_numbers(4, 3) == 12 

def test_minus_numbers():
    assert math_lib.mul_numbers(4, 3) == 5 




