from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_6820():
    assert remove_extras([3, 4, 4]) == [3, 4]
