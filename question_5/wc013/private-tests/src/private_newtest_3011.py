from wrong_correct_5_013 import *

import pytest
@pytest.mark.timeout(5)
def test_3011():
    assert top_k([5, 7],1) == [7]
