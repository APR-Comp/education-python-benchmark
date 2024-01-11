from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_8918():
    assert sort_age([('M', 29), ('M', 37)]) == [('M', 37), ('M', 29)]
