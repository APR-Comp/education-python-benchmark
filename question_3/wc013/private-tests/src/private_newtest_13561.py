from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_13561():
    assert remove_extras([6]) == [6]