from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17669():
    assert sort_age([('F', 10)]) == [('F', 10)]
