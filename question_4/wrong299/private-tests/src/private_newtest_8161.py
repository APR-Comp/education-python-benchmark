from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_8161():
    assert sort_age([('M', 1)]) == [('M', 1)]
