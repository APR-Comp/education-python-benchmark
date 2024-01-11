from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_11653():
    assert top_k([6],0) == []
