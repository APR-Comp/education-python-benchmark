from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_5729():
    assert remove_extras([2826]) == [2826]
