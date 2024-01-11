from wrong_4_334 import *

import pytest
@pytest.mark.timeout(5)
def test_16300():
    assert sort_age([('M', 19)]) == [('M', 19)]
