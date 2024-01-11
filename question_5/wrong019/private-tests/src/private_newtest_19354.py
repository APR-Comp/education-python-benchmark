from wrong_5_019 import *

import pytest
@pytest.mark.timeout(5)
def test_19354():
    assert top_k([2],0) == []
