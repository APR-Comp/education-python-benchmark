from wrong_correct_5_040 import *

import pytest
@pytest.mark.timeout(5)
def test_12557():
    assert top_k([56, 7],0) == []
