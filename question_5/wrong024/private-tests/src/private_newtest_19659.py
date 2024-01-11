from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_19659():
    assert top_k([7, 24, 2],0) == []
