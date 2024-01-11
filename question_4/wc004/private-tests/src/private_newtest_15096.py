from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_15096():
    assert sort_age([('M', 8)]) == [('M', 8)]
