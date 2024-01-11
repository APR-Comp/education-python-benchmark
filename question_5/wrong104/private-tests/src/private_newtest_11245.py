from wrong_5_104 import *

import pytest
@pytest.mark.timeout(5)
def test_11245():
    assert top_k([1],0) == []
