from wrong_5_059 import *

import pytest
@pytest.mark.timeout(5)
def test_5761():
    assert top_k([251, 8],1) == [251]
