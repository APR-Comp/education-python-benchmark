from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_7025():
    assert sort_age([('M', 38)]) == [('M', 38)]
