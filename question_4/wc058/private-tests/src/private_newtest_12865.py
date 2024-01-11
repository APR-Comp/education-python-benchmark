from wrong_correct_4_058 import *

import pytest
@pytest.mark.timeout(5)
def test_12865():
    assert sort_age([('M', 39)]) == [('M', 39)]
