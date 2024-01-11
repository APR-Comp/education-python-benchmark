from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_2872():
    assert top_k([3, 29, 8, 8696],2) == [8696, 29]
