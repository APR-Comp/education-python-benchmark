from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_15471():
    assert remove_extras([9]) == [9]
