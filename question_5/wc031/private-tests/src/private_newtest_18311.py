from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_18311():
    assert top_k([5],0) == []