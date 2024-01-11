from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_10539():
    assert sort_age([('M', 9)]) == [('M', 9)]
