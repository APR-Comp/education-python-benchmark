from wrong_5_074 import *

import pytest
@pytest.mark.timeout(5)
def test_15913():
    assert top_k([54, 96, 331, 2],0) == []
