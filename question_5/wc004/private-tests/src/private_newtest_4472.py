from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_4472():
    assert top_k([9],0) == []