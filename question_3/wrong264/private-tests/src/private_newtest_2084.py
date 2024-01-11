from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_2084():
    assert remove_extras([5]) == [5]
