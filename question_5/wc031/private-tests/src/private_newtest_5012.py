from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_5012():
    assert top_k([2],0) == []
