from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_11296():
    assert top_k([33432, 69],0) == []
