from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_7061():
    assert top_k([5],0) == []
