from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_3454():
    assert sort_age([('F', 34)]) == [('F', 34)]
