from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_10716():
    assert remove_extras([1, 6]) == [1, 6]
