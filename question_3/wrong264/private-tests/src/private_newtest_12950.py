from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_12950():
    assert remove_extras([728]) == [728]
