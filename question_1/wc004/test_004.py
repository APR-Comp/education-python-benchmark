
from wrong_correct_1_004 import *
import pytest
@pytest.mark.timeout(5)
def test_004():
    assert search(7, [1, 5, 10]) == 2
