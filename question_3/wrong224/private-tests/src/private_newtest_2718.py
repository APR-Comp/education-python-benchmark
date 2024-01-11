from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_2718():
    assert remove_extras([2, 94]) == [2, 94]
