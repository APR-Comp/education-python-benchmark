from wrong_5_049 import *

import pytest
@pytest.mark.timeout(5)
def test_15467():
    assert top_k([8],0) == []
