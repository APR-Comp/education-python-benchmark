from wrong_5_054 import *

import pytest
@pytest.mark.timeout(5)
def test_415():
    assert top_k([7, 2, 14],0) == []
