from wrong_correct_4_040 import *

import pytest
@pytest.mark.timeout(5)
def test_3908():
    assert sort_age([('F', 9)]) == [('F', 9)]
