from wrong_correct_4_013 import *

import pytest
@pytest.mark.timeout(5)
def test_19557():
    assert sort_age([('M', 7), ('F', 8)]) == [('F', 8), ('M', 7)]