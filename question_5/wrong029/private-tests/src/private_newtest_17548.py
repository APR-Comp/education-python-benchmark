from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_17548():
    assert top_k([172],0) == []
