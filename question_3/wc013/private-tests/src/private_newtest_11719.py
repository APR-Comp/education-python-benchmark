from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_11719():
    assert remove_extras([1]) == [1]
