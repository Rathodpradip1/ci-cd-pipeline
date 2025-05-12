from src.main import add,substract

def test_add_function():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(5, 5) == 10

def test_substract_function():
    assert substract(5 ,5) == 0
    assert substract(10, 2) == 8
    assert substract(0, 0) == 0
