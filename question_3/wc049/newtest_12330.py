from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_12330():
    assert remove_extras([1]) == [1]
