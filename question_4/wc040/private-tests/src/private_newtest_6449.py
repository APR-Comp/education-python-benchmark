from wrong_correct_4_040 import *

import pytest
@pytest.mark.timeout(5)
def test_6449():
    assert sort_age([('M', 9)]) == [('M', 9)]
