from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_12749():
    assert top_k([9],0) == []