from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_2260():
    assert sort_age([('F', 9)]) == [('F', 9)]
