from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_10602():
    assert remove_extras([88, 9, 2, 37]) == [88, 9, 2, 37]
