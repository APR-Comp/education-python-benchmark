from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_12387():
    assert top_k([7633],0) == []
