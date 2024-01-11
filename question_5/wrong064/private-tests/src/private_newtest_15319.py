from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_15319():
    assert top_k([9, 4, 48],0) == []
