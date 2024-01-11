from wrong_5_084 import *

import pytest
@pytest.mark.timeout(5)
def test_12186():
    assert top_k([2],0) == []
