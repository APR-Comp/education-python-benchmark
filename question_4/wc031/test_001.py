
from wrong_correct_4_031 import *
import pytest
@pytest.mark.timeout(5)
def test_001():
    assert sort_age([("F", 19)]) == [('F', 19)]
