from wrong_correct_5_022 import *

import pytest
@pytest.mark.timeout(5)
def test_779():
    assert top_k([32950, 9, 939],1) == [32950]
