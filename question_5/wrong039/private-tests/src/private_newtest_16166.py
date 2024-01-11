from wrong_5_039 import *

import pytest
@pytest.mark.timeout(5)
def test_16166():
    assert top_k([3, 5, 42],0) == []
