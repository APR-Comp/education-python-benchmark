from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_2279():
    assert sort_age([('F', 17)]) == [('F', 17)]
