from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_6203():
    assert top_k([84, 42],0) == []
