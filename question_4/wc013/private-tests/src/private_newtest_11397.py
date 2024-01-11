from wrong_correct_4_013 import *

import pytest
@pytest.mark.timeout(5)
def test_11397():
    assert sort_age([('M', 6)]) == [('M', 6)]
