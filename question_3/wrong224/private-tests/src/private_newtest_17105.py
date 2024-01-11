from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_17105():
    assert remove_extras([26, 41]) == [26, 41]
