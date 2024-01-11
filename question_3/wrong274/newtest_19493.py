from wrong_3_274 import *

import pytest
@pytest.mark.timeout(5)
def test_19493():
    assert remove_extras([2, 8448, 9, 6]) == [2, 8448, 9, 6]
