from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_13366():
    assert top_k([6, 8],1) == [8]
