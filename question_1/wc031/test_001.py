
from wrong_correct_1_031 import *
import pytest
@pytest.mark.timeout(5)
def test_001():
    assert search(42, (-5, 1, 3, 5, 7, 10)) == 6