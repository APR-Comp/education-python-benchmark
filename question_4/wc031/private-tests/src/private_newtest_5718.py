from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_5718():
    assert sort_age([('F', 39)]) == [('F', 39)]
