from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_17389():
    assert remove_extras([9]) == [9]
