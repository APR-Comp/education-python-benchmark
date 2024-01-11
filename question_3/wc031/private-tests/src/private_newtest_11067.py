from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_11067():
    assert remove_extras([5, 2, 4296, 795661046, 4]) == [5, 2, 4296, 795661046, 4]
