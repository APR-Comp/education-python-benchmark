from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_12292():
    assert top_k([9180067310],0) == []
