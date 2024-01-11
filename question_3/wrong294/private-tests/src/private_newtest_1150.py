from wrong_3_294 import *

import pytest
@pytest.mark.timeout(5)
def test_1150():
    assert remove_extras([4, 8, 6]) == [4, 8, 6]
