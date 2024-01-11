from wrong_correct_4_058 import *

import pytest
@pytest.mark.timeout(5)
def test_15096():
    assert sort_age([('M', 8)]) == [('M', 8)]
