from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_1903():
    assert search(43,[3, 7, 3271]) == 2
