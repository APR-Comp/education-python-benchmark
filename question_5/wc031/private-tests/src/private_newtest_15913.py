from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_15913():
    assert top_k([54, 96, 331, 2],0) == []
