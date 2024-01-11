from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_5012():
    assert top_k([2],0) == []
