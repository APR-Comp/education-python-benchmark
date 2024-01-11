from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_320():
    assert sort_age([('F', 5)]) == [('F', 5)]
