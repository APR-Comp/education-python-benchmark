from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_437():
    assert sort_age([('M', 1)]) == [('M', 1)]
