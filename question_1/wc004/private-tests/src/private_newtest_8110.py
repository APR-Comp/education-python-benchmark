from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_8110():
    assert search(74,[4, 67, 75]) == 2
