from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_6956():
    assert remove_extras([2, 6]) == [2, 6]
