from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_12427():
    assert sort_age([('M', 2)]) == [('M', 2)]
