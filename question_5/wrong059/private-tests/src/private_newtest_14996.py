from wrong_5_059 import *

import pytest
@pytest.mark.timeout(5)
def test_14996():
    assert top_k([6, 917886, 4, 206],2) == [917886, 206]
