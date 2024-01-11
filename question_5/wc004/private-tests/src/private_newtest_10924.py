from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_10924():
    assert top_k([2, 98, 74],1) == [98]
