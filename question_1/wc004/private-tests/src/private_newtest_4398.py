from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_4398():
    assert search(73,[5, 6, 670, 1535, 8769]) == 2