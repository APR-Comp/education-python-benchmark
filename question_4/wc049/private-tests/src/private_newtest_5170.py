from wrong_correct_4_049 import *

import pytest
@pytest.mark.timeout(5)
def test_5170():
    assert sort_age([('M', 2)]) == [('M', 2)]