
from wrong_correct_1_004 import *
import pytest
@pytest.mark.timeout(5)
def test_005():
    assert search(3, (1, 5, 10)) == 1
