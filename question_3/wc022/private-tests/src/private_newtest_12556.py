from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_12556():
    assert remove_extras([80370, 9]) == [80370, 9]
