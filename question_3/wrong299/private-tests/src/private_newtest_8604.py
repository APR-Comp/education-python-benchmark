from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_8604():
    assert remove_extras([96, 4, 9]) == [96, 4, 9]