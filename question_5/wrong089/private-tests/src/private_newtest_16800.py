from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_16800():
    assert top_k([9],0) == []
