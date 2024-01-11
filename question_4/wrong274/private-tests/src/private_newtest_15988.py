from wrong_4_274 import *

import pytest
@pytest.mark.timeout(5)
def test_15988():
    assert sort_age([('F', 6), ('F', 4)]) == [('F', 6), ('F', 4)]
