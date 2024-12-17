'''import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.main import subtract

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(1, -1) == 2
    assert subtract(1, 0) == 1'''
