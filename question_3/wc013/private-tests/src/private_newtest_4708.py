from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_4708():
    assert remove_extras([5]) == [5]
