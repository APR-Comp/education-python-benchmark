from wrong_3_284 import *

import pytest
@pytest.mark.timeout(5)
def test_5662():
    assert remove_extras([2, 1, 6, 7438, 84, 3, 7]) == [2, 1, 6, 7438, 84, 3, 7]
