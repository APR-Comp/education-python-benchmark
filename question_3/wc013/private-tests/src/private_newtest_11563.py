from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_11563():
    assert remove_extras([7]) == [7]
