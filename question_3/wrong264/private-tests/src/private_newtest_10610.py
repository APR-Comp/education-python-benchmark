from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_10610():
    assert remove_extras([163, 8]) == [163, 8]
