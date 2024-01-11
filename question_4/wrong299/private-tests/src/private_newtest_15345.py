from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_15345():
    assert sort_age([('M', 19)]) == [('M', 19)]
