from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_4142():
    assert top_k([2],0) == []
