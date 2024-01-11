from wrong_3_304 import *

import pytest
@pytest.mark.timeout(5)
def test_11387():
    assert remove_extras([4, 69, 4, 5]) == [4, 69, 5]
