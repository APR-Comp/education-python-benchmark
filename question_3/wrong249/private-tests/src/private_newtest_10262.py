from wrong_3_249 import *

import pytest
@pytest.mark.timeout(5)
def test_10262():
    assert remove_extras([3, 92, 25, 36, 14, 9, 34]) == [3, 92, 25, 36, 14, 9, 34]
