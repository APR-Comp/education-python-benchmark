from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_4933():
    assert top_k([1, 9, 3, 6],1) == [9]
