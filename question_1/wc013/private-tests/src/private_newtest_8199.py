from wrong_correct_1_013 import *

import pytest
@pytest.mark.timeout(5)
def test_8199():
    assert search(43,[3, 5]) == 2
