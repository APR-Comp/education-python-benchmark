from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_1801():
    assert remove_extras([4307]) == [4307]
