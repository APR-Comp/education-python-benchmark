from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_11296():
    assert top_k([33432, 69],0) == []
