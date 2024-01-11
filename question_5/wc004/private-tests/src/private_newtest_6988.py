from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_6988():
    assert top_k([486, 1, 8],0) == []
