from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_4444():
    assert sort_age([('M', 5), ('M', 8)]) == [('M', 8), ('M', 5)]
