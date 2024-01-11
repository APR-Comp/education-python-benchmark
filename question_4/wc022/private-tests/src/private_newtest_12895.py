from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_12895():
    assert sort_age([('F', 2)]) == [('F', 2)]
