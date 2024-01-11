from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_6320():
    assert top_k([4, 77],1) == [77]
