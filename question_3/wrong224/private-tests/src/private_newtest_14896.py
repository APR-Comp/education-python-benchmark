from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_14896():
    assert remove_extras([8, 8, 9]) == [8, 9]
