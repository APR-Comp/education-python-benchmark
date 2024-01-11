from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_8833():
    assert remove_extras([8]) == [8]
