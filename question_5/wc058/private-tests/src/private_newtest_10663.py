from wrong_correct_5_058 import *

import pytest
@pytest.mark.timeout(5)
def test_10663():
    assert top_k([1, 1, 614],0) == []
