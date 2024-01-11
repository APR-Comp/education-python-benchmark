from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_11245():
    assert top_k([1],0) == []
