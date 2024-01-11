from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_10841():
    assert top_k([61, 62],0) == []
