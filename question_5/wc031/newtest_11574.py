from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_11574():
    assert top_k([7, 8],1) == [8]
