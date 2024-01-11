from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_19659():
    assert top_k([7, 24, 2],0) == []
