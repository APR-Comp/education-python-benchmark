from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_2139():
    assert remove_extras([85, 8, 8]) == [85, 8]
