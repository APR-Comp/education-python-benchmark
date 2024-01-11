from wrong_3_304 import *

import pytest
@pytest.mark.timeout(5)
def test_1150():
    assert remove_extras([4, 8, 6]) == [4, 8, 6]
