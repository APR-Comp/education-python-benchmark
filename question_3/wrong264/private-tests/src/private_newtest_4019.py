from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_4019():
    assert remove_extras([2, 6, 5]) == [2, 6, 5]
