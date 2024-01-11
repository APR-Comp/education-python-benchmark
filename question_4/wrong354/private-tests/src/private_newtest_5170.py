from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_5170():
    assert sort_age([('M', 2)]) == [('M', 2)]
