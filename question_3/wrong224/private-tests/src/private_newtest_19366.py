from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_19366():
    assert remove_extras([6]) == [6]
