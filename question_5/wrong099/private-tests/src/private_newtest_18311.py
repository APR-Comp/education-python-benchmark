from wrong_5_099 import *

import pytest
@pytest.mark.timeout(5)
def test_18311():
    assert top_k([5],0) == []
