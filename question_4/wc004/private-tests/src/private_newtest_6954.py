from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_6954():
    assert sort_age([('F', 3)]) == [('F', 3)]
