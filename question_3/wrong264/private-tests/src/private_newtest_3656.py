from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_3656():
    assert remove_extras([2, 31]) == [2, 31]
