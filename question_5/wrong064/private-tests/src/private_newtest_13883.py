from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_13883():
    assert top_k([3, 3, 12],1) == [12]
