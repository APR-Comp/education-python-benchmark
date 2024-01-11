from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_15345():
    assert sort_age([('M', 19)]) == [('M', 19)]
