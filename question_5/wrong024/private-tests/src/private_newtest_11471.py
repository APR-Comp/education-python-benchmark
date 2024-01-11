from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_11471():
    assert top_k([38, 4],1) == [38]
