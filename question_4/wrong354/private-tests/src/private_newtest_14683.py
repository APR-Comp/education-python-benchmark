from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_14683():
    assert sort_age([('M', 10)]) == [('M', 10)]
