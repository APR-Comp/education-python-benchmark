from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_6142():
    assert top_k([9, 3],1) == [9]
