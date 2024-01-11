from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_2829():
    assert search(4,[6, 219, 1930]) == 0
