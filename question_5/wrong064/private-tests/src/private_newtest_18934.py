from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_18934():
    assert top_k([2167, 806],1) == [2167]
