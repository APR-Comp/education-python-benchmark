from wrong_4_274 import *

import pytest
@pytest.mark.timeout(5)
def test_16612():
    assert sort_age([('F', 5), ('F', 8)]) == [('F', 8), ('F', 5)]
