from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_6320():
    assert top_k([4, 77],1) == [77]
