from wrong_4_329 import *

import pytest
@pytest.mark.timeout(5)
def test_18484():
    assert sort_age([('M', 4)]) == [('M', 4)]
