from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_9018():
    assert sort_age([('M', 12)]) == [('M', 12)]
