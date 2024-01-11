from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_14683():
    assert sort_age([('M', 10)]) == [('M', 10)]
