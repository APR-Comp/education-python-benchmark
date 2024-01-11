from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_3805():
    assert remove_extras([9, 2156]) == [9, 2156]
