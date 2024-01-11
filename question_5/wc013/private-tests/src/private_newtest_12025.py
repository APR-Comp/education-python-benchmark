from wrong_correct_5_013 import *

import pytest
@pytest.mark.timeout(5)
def test_12025():
    assert top_k([1556, 17],1) == [1556]
