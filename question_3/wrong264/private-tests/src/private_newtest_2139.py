from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_2139():
    assert remove_extras([85, 8, 8]) == [85, 8]
