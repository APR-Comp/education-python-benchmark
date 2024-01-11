from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_10841():
    assert top_k([61, 62],0) == []
