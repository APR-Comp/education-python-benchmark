from wrong_correct_1_040 import *

import pytest
@pytest.mark.timeout(5)
def test_8463():
    assert search(730,[6, 9, 31, 353, 642]) == 5
