from wrong_3_259 import *

import pytest
@pytest.mark.timeout(5)
def test_11866():
    assert remove_extras([9, 1, 1, 8]) == [9, 1, 8]
