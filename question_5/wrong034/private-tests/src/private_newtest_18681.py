from wrong_5_034 import *

import pytest
@pytest.mark.timeout(5)
def test_18681():
    assert top_k([30],0) == []
