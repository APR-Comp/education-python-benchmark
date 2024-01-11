from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_4374():
    assert remove_extras([3, 7]) == [3, 7]
