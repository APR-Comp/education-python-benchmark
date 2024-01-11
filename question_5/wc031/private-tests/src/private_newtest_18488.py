from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_18488():
    assert top_k([2, 1],1) == [2]
