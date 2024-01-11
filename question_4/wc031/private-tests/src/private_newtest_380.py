from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_380():
    assert sort_age([('F', 7)]) == [('F', 7)]
