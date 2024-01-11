from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_12653():
    assert remove_extras([6, 2]) == [6, 2]
