from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_15851():
    assert top_k([508],0) == []
