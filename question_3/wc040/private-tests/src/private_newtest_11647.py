from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_11647():
    assert remove_extras([9, 3]) == [9, 3]
