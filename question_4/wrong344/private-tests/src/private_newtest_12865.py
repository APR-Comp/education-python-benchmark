from wrong_4_344 import *

import pytest
@pytest.mark.timeout(5)
def test_12865():
    assert sort_age([('M', 39)]) == [('M', 39)]
