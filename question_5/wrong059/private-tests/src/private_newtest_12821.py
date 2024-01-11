from wrong_5_059 import *

import pytest
@pytest.mark.timeout(5)
def test_12821():
    assert top_k([82, 4, 5],2) == [82, 5]
