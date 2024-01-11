from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_11371():
    assert remove_extras([39, 66]) == [39, 66]
