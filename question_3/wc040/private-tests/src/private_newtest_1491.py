from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_1491():
    assert remove_extras([9]) == [9]
