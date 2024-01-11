from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_14764():
    assert sort_age([('M', 4)]) == [('M', 4)]
