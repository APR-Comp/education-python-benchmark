from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_12950():
    assert remove_extras([728]) == [728]
