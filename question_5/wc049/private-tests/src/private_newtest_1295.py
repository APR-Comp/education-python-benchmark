from wrong_correct_5_049 import *

import pytest
@pytest.mark.timeout(5)
def test_1295():
    assert top_k([2, 6, 1],2) == [6, 2]
