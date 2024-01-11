from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_19497():
    assert top_k([1, 4, 48, 15, 3, 56],3) == [56, 48, 15]
