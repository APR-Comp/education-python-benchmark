from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_8551():
    assert top_k([67, 3601, 5],2) == [3601, 67]
