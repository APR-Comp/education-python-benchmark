from wrong_correct_1_013 import *

import pytest
@pytest.mark.timeout(5)
def test_8025():
    assert search(51,[4, 5, 7, 53]) == 3
