from wrong_5_079 import *

import pytest
@pytest.mark.timeout(5)
def test_14800():
    assert top_k([3, 57547, 41],2) == [57547, 41]
