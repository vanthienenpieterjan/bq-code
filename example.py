import pytest

def add(a,b):
  return a+b

def substract(a,b):
  return a * b


## Imagine I made a valid change

def absolut(a,b):
  return np.abs(a,b)
def test_add():
    exres=10
    assert abs(add(6,4)-exres)<0.001
