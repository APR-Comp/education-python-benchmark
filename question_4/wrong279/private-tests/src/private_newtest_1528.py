from wrong_4_279 import *

import pytest
@pytest.mark.timeout(5)
def test_1528():
    assert sort_age([('M', 33)]) == [('M', 33)]