from wrong_correct_4_013 import *

import pytest
@pytest.mark.timeout(5)
def test_3539():
    assert sort_age([('F', 11)]) == [('F', 11)]
