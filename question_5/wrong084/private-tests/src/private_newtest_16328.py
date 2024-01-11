from wrong_5_084 import *

import pytest
@pytest.mark.timeout(5)
def test_16328():
    assert top_k([9717, 3, 8, 1],1) == [9717]
