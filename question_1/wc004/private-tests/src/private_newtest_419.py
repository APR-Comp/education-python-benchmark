from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_419():
    assert search(3,[1, 2, 6]) == 2
