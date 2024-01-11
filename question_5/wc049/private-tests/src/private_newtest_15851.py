from wrong_correct_5_049 import *

import pytest
@pytest.mark.timeout(5)
def test_15851():
    assert top_k([508],0) == []
