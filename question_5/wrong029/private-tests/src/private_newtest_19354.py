from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_19354():
    assert top_k([2],0) == []
