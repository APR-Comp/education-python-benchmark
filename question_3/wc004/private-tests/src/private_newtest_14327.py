from wrong_correct_3_004 import *

import pytest
@pytest.mark.timeout(5)
def test_14327():
    assert remove_extras([4]) == [4]
