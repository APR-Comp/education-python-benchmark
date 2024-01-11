from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_12371():
    assert top_k([1, 85],1) == [85]
