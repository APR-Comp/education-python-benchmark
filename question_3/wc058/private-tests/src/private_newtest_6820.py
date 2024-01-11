from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_6820():
    assert remove_extras([3, 4, 4]) == [3, 4]
