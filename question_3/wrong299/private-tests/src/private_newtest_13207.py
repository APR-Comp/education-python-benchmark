from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_13207():
    assert remove_extras([2]) == [2]
