from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_2694():
    assert sort_age([('F', 32)]) == [('F', 32)]
