from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_11719():
    assert remove_extras([1]) == [1]
