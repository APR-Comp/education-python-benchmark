from wrong_5_079 import *

import pytest
@pytest.mark.timeout(5)
def test_16765():
    assert top_k([1, 3],0) == []
