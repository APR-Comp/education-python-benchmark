from wrong_3_254 import *

import pytest
@pytest.mark.timeout(5)
def test_18470():
    assert remove_extras([7]) == [7]
