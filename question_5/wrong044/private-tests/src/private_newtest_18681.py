from wrong_5_044 import *

import pytest
@pytest.mark.timeout(5)
def test_18681():
    assert top_k([30],0) == []