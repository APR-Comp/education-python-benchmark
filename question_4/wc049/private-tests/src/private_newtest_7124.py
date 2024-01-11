from wrong_correct_4_049 import *

import pytest
@pytest.mark.timeout(5)
def test_7124():
    assert sort_age([('M', 20)]) == [('M', 20)]
