from wrong_5_069 import *

import pytest
@pytest.mark.timeout(5)
def test_8260():
    assert top_k([2],0) == []
