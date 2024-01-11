from wrong_3_259 import *

import pytest
@pytest.mark.timeout(5)
def test_10716():
    assert remove_extras([1, 6]) == [1, 6]
