from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_11342():
    assert top_k([861, 89],0) == []
