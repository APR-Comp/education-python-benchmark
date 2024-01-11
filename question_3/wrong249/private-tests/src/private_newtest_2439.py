from wrong_3_249 import *

import pytest
@pytest.mark.timeout(5)
def test_2439():
    assert remove_extras([1, 168, 81, 4]) == [1, 168, 81, 4]
