from wrong_correct_4_013 import *

import pytest
@pytest.mark.timeout(5)
def test_16079():
    assert sort_age([('F', 11)]) == [('F', 11)]
