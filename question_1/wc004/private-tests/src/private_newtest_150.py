from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_150():
    assert search(8,[3, 6, 8, 19, 94]) == 2
