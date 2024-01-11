from wrong_3_284 import *

import pytest
@pytest.mark.timeout(5)
def test_1134():
    assert remove_extras([1, 33348, 7, 2]) == [1, 33348, 7, 2]
