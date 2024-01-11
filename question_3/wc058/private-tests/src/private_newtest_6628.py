from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_6628():
    assert remove_extras([3, 44]) == [3, 44]
