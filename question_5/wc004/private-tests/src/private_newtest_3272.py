from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_3272():
    assert top_k([21],0) == []
