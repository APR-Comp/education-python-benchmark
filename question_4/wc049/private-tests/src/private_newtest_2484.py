from wrong_correct_4_049 import *

import pytest
@pytest.mark.timeout(5)
def test_2484():
    assert sort_age([('M', 22)]) == [('M', 22)]
