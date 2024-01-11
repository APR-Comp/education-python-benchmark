from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_18278():
    assert remove_extras([3, 18]) == [3, 18]
