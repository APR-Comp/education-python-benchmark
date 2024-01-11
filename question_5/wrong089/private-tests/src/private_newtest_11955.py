from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_11955():
    assert top_k([1],0) == []
