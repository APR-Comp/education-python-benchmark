from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_11249():
    assert remove_extras([104, 331, 4, 177, 5, 4]) == [104, 331, 4, 177, 5]
