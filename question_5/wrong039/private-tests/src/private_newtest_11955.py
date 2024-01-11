from wrong_5_039 import *

import pytest
@pytest.mark.timeout(5)
def test_11955():
    assert top_k([1],0) == []
