from wrong_3_259 import *

import pytest
@pytest.mark.timeout(5)
def test_10299():
    assert remove_extras([3, 987]) == [3, 987]
