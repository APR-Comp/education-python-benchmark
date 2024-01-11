from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_16003():
    assert remove_extras([4]) == [4]
