from wrong_correct_3_004 import *

import pytest
@pytest.mark.timeout(5)
def test_12345():
    assert remove_extras([9]) == [9]
