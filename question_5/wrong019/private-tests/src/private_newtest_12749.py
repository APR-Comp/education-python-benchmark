from wrong_5_019 import *

import pytest
@pytest.mark.timeout(5)
def test_12749():
    assert top_k([9],0) == []
