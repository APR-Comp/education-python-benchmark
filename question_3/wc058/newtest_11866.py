from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_11866():
    assert remove_extras([9, 1, 1, 8]) == [9, 1, 8]
