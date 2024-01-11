from wrong_3_269 import *

import pytest
@pytest.mark.timeout(5)
def test_13521():
    assert remove_extras([83, 30, 889, 405]) == [83, 30, 889, 405]
