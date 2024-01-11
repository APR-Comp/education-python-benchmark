from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_10041():
    assert top_k([401],0) == []
