from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_6661():
    assert sort_age([('M', 30)]) == [('M', 30)]
